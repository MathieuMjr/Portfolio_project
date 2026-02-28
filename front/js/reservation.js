import { fetchCurrentUser, getCookie } from "./auth.js";
import { setHeader } from "./header.js";
import { fetchStatus, fetchThemes, fetchAudienceTypes} from "./api.js";

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

const test = [
    {
        id: "pouet",
        name: "pouet"
    },
    {
        id:"good",
        name:"good"
    }];


const token = getCookie('token');

document.addEventListener('DOMContentLoaded', async () => {
    if (!token) {
            window.location.href = '../html/index.html'
        }

     // header   
    const responseHeader = await fetch('../html/header.html');
    const headerContent = await responseHeader.text();
    const header = document.querySelector(".navigation");
    header.innerHTML = headerContent;
    
    // fetches
    const [identity, audienceTypes, statuses] = await Promise.all([
        safeFetch(fetchCurrentUser),
        safeFetch(fetchAudienceTypes),
        safeFetch(fetchStatus),
    ])

    // Header, reservation types, themes
    if (identity) {
        setHeader(identity);
        displayResTypes(identity.reservation_types);

        const resTypeSelect = document.getElementById('res_type');
        resTypeSelect.addEventListener('change', async (e) => {
            payload.reservation_type_id = e.target.value;
            console.log(payload);

            const themeList = await safeFetch(fetchThemes, e.target.value);
            if (themeList) {
                console.log(themeList);
                displayThemes(themeList);
            }
        })
    }

    if (statuses) {
        displayStatus(statuses);
    }

    if (audienceTypes) {
        displayAudienceTypes(audienceTypes);
    }

    displayStructType(test);
    displayStruct(test);

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
        })
    })
    // document.getElementById('struct_type').addEventListener('change', (event) => {
    //     payload.structure_id = event.target.value;
    //     console.log(payload);
    // })


// --- DISPLAY FUNCTIONS    

// -- RESERVATION TYPES
function displayResTypes(data) {
    const ResTypeContainer = document.querySelector('.res_type');

    const resTypeField = document.createElement('div');
    resTypeField.classList.add('field');

    const resTypeLabel = document.createElement('label');
    resTypeLabel.setAttribute('for', 'res_type');
    // resTypeLabel.textContent ='Type de réservation';
    resTypeField.appendChild(resTypeLabel);

    const resTypeSelect = document.createElement('select');
    resTypeSelect.id ='res_type';
    resTypeSelect.name = 'res_type';

    const resTypeChoose = document.createElement('option');
    resTypeChoose.value = "";
    resTypeChoose.textContent = "Choisir le type de réservation";
    resTypeSelect.appendChild(resTypeChoose);

    data.forEach((element) => {
        const option = document.createElement('option');
        option.value = element.id;
        option.innerText = element.name;
        resTypeSelect.appendChild(option);
    })

    resTypeField.appendChild(resTypeSelect);
    ResTypeContainer.appendChild(resTypeField);
}

// -- STATUSES
function displayStatus(data) {
    const statusContainer = document.querySelector('.status');
    const statusField = document.createElement('div');
    statusField.classList.add('field');

    const statusLabel = document.createElement('label');
    statusLabel.setAttribute('for', 'status');
    statusField.appendChild(statusLabel);
    
    const statusSelect = document.createElement('select');
    statusSelect.id = "status";
    statusSelect.name = "status";

    const defaultOption = document.createElement('option');
    defaultOption.value ="";
    defaultOption.textContent = "Choisir le statut";
    statusSelect.appendChild(defaultOption);

    data.forEach((element) => {
        const option = document.createElement('option');
        option.value = element.id;
        option.textContent = element.name;
        statusSelect.appendChild(option);
    })

    statusField.appendChild(statusSelect);
    statusContainer.appendChild(statusField);
}

// -- THEMES
function displayThemes(data) {
    const themeContainer = document.querySelector('.theme');
    themeContainer.innerHTML = "";
    data.forEach((element) => {
        const field = document.createElement('field');
        const input = document.createElement('input');
        input.type = "checkbox";
        input.id = `theme_${element.id}`;
        input.name = "themes";
        input.value = element.id;
        const label = document.createElement('label');
        label.setAttribute('for', `theme_${element.id}`);
        label.textContent = element.name;
        field.appendChild(input);
        field.appendChild(label);
        themeContainer.appendChild(field);
    })
}

// STRUCTURE TYPES
function displayStructType(data) {
    const select = document.getElementById('struct_type');
    data.forEach((element) => {
        const option = document.createElement('option');
        option.value = element.id;
        option.textContent = element.name;
        select.appendChild(option);
    })
}

// STRUCTURES
function displayStruct(data) {
    const select = document.getElementById('struct_name');
    data.forEach((element) => {
        const option = document.createElement('option');
        option.value = element.id;
        option.textContent = element.name;
        select.appendChild(option);
    })
}

// -- AUDIENCE TYPES
function displayAudienceTypes(data) {
    const audienceForm = document.querySelector('.audience_form');
    const categories = [];
    // extrait les catégories existantes
    data.forEach((element) => {
        if (!categories.includes(element.category)) {
            categories.push(element.category);
        }
    });
    // pour chaque catégorie, créer les div, titres et champs
    categories.forEach((element) => {
        // Selectionner les data de la catégorie
        const categoryData = data.filter((n) => n.category === element);
        const sortedData = categoryData.sort((a, b) => a.order_index - b.order_index);
        //Créer la div de la catégorie
        const categoryDiv = document.createElement('div');
        categoryDiv.classList.add("category");
        const title = document.createElement('h3');
        title.textContent = element;
        categoryDiv.appendChild(title);
        // Pour chaque data de la catégorie :
        sortedData.forEach((data) => {
            const field = document.createElement('div');
            field.classList.add('field');
            const label = document.createElement('label');
            label.setAttribute('for', data.name);
            label.innerText = data.name;
            field.appendChild(label);
            const input = document.createElement('input');
            input.type = "number";
            input.id = data.name;
            input.name = "audience";
            input.dataset.audienceT_id = data.id;
            field.appendChild(input);
            categoryDiv.appendChild(field);
        });
        audienceForm.appendChild(categoryDiv);
    });
}

async function safeFetch(fetchFunction, ...arg) {
    try{
        return await fetchFunction(...arg);
    } catch (error) {
        alert(error.message);
        return null;
    }
}