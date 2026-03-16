import { fetchCurrentUser, getCookie } from "./auth.js";
import { setHeader } from "./header.js";
import { fetchStatus,
    fetchThemes,
    fetchAudienceTypes,
    fetchStructureTypes, 
    fetchStructures,
    postReservation,
    fetchReservation, 
    putReservation} from "./api.js";

import { displayAudienceTypes,
    displayExistingRes,
    displayResTypes,
    displayStatus,
    displayStructDetails,
    displayStructNames,
    displayStructType,
    displayThemes} from "./reservation_ui.js";

const payload = {
    "structure_id": null,
    "reservation_type_id": null,
    "reservation_date": null,
    "hour": null,
    "contact_firstname": null,
    "contact_lastname": null,
    "contact_phone": null,
    "contact_email": null,
    "contact_role": null,
    "price": null,
    "status_id": null,
    "themes_id_list": [],
    "audiences": []
};

// Liste des champs : permet de ne pas ajouter aux payloads certains
// input du formulaire lors d'un change detecté par eventlistener
const payloadFields = [
    "structure_id", "reservation_type_id", "reservation_date",
    "hour", "contact_firstname", "contact_lastname",
    "contact_phone", "contact_email", "contact_role", "price", "status_id",
    "themes_id_list", "audiences"
]

const token = getCookie('token');

document.addEventListener('DOMContentLoaded', async () => {
    if (!token) {
        window.location.href = '../html/index.html'
    }

    const urlParams = new URLSearchParams(window.location.search);
    const reservationId = urlParams.get('id');

     // header   
    const responseHeader = await fetch('../html/header.html');
    const headerContent = await responseHeader.text();
    const header = document.querySelector(".navigation");
    header.innerHTML = headerContent;
    
    // fetches
    let identity, audienceTypes, statuses, structT;
    try {
        [identity, audienceTypes, statuses, structT] = await Promise.all([
        fetchCurrentUser(),
        fetchAudienceTypes(),
        fetchStatus(),
        fetchStructureTypes(),
        ])
    } catch(error) {
        alert(error.message);
        window.location.href = '../html/index.html'
    }
    
    // Header, reservation types, themes
    if (identity) {
        setHeader(identity);
        console.log(identity);
        displayResTypes(identity.reservation_types);

        const resTypeSelect = document.getElementById('res_type');
        resTypeSelect.addEventListener('change', async (e) => {
            payload.reservation_type_id = e.target.value;
            payload.themes_id_list = [];
            console.log(payload);

            const themeList = await safeFetch(fetchThemes, e.target.value);
            if (themeList) {
                console.log(themeList);
                displayThemes(themeList);
            }
        })
    }
    document.getElementById("logout").addEventListener("click", () => {
    document.cookie = "token=; Max-Age=0; path=/";
    window.location.href = "../html/index.html";
    });

    if (statuses) {
        displayStatus(statuses);
    }

    if (audienceTypes) {
        displayAudienceTypes(audienceTypes);
    }

    if (structT) {
        displayStructType(structT);
        let structT_id, zipCode;
        document.getElementById('struct_type').addEventListener(
            'change', async (event) => {
                structT_id = event.target.value;
                const structures = await safeFetch(fetchStructures, structT_id, zipCode);
                if (structures) displayStructNames(structures);
            }
        )
        document.getElementById('struct_zip').addEventListener(
            'change', async (event) => {
                zipCode = event.target.value;
                const structures = await safeFetch(fetchStructures, structT_id, zipCode);
                if (structures) displayStructNames(structures);
            }
        )
    }

    // Event listener and paylaod construction
    document.querySelector('.form_container').addEventListener(
        'change', (event) => {
            const input = event.target;
            // Si est un champs date, heure ou de contact
            if (input.matches(
                "input[type='number'], input[type='text'], input[type='date'], input[type='time'], input[type='email'], input[type='tel']") && payloadFields.includes(input.name)) {
                payload[input.name] = input.value;
                console.log(payload);
            }
            // Si est un champs d'audience
            else if (input.matches("input[type='number'][name='audience']")) {
                const audienceId = input.dataset.audienceT_id;
                const audienceNumber = Number(event.target.value);

                if (audienceNumber > 0) {
                    const existingAudience = payload.audiences.find(
                        (element) => element.audienceT_id === audienceId);
                    if (existingAudience) {
                        existingAudience.count = audienceNumber;
                    } else {
                        payload.audiences.push({
                            "count": audienceNumber,
                            "audience_type_id": audienceId
                        });
                    }
                } else {
                    payload.audiences = payload.audiences.filter(
                        (element) => element.audience_type_id !== audienceId);
                }
                console.log(payload);
            }
            // si est un status
            else if (input.matches("#status")) {
                payload.status_id = input.value;
                console.log(payload);
            }
            // si est un thème coché/décoché
            else if (input.matches("[name=themes]")) {
                if (input.checked) {
                    payload.themes_id_list.push(input.value);
                } else {
                    payload.themes_id_list = payload.themes_id_list.filter(
                        id => id !== input.value);
                }
                console.log(payload);
            }
            // si une sutructure est selectionnée 
            else if (input.matches("#struct_name")) {
                payload.structure_id = input.value;
                const selectedOption = input.selectedOptions[0];
                const address = selectedOption.dataset.address;
                console.log(address);
                const town = selectedOption.dataset.town;
                const email = selectedOption.dataset.email;
                const phone = selectedOption.dataset.phone;
                displayStructDetails(address, town, email, phone);
                console.log(payload);
            }
    })

    if (reservationId) {
        try {
            const resDetails = await fetchReservation(reservationId);
            displayExistingRes(resDetails);
            payloadFromExistingRes(resDetails, payload);
            console.log(payload);
        } catch (error) {
            alert(error.message);
        }  
    }

    document.querySelector('.form_container').addEventListener(
        'submit', async (event) => {
            event.preventDefault();
            if (!checkPayload(payload)) {
                alert("Champs manquant(s) ou invalide(s)");
                return;
            }
            if (reservationId) {
                const response = await safeFetch(putReservation, payload, reservationId);
                if (response) {
                    console.log(response);
                    alert("Réservation mise à jour avec succès");
                    window.location.href = "../html/planning.html";
                }
            } else {
                const response = await safeFetch(postReservation, payload);
                if (response) {
                    alert('Réservation créée avec succès');
                    window.location.href = "../html/planning.html";
                }
            }
        }
    )
})

// Util function
async function safeFetch(fetchFunction, ...arg) {
    try{
        return await fetchFunction(...arg);
    } catch (error) {
        alert(error.message);
        return null;
    }
}

function checkPayload(payload) {
    return Object.entries(payload).every(([key, value]) => {
    if (Array.isArray(value)) return value.length > 0;
    return value !== null && value !== "";
})
}

function payloadFromExistingRes(resDetails, payload) {
    payload.structure_id = resDetails.structure.id;
    payload.reservation_type_id = resDetails.reservation_type.id;
    payload.reservation_date = resDetails.reservation_date;
    payload.hour = resDetails.hour;
    payload.contact_firstname = resDetails.contact.firstname;
    payload.contact_lastname = resDetails.contact.lastname;
    payload.contact_phone = resDetails.contact.phone;
    payload.contact_email = resDetails.contact.email;
    payload.contact_role = resDetails.contact.role;
    payload.price = resDetails.price;
    payload.status_id = resDetails.status.id;
    resDetails.themes.forEach((theme) => {
        payload.themes_id_list.push(theme.id);
    });
    resDetails.audiences.forEach((audience) => {
        const audienceDict = {
            "count": audience.count,
            "audience_type_id": audience.audience_type.id
        };
        payload.audiences.push(audienceDict);
    });
    payload.author_id = resDetails.author.id;
}