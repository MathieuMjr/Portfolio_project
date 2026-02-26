import { API_BASE_URL } from "./config.js";
import { fetchCurrentUser, getCookie } from "./auth.js";
import { setHeader } from "./header.js";
import { fetchStatus, fetchThemes } from "./api.js";

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
const test = [
    {
        id: "pouet",
        name: "pouet"
    },
    {
        id:"good",
        name:"good"
    }];
    console.log(test);

const token = getCookie('token');

document.addEventListener('DOMContentLoaded', async () => {
    if (!token) {
            window.location.href = '../html/index.html'
        }
    const responseHeader = await fetch('../html/header.html');
    const headerContent = await responseHeader.text();
    const header = document.querySelector(".navigation");
    header.innerHTML = headerContent;
    try {
        const identity = await fetchCurrentUser();
        setHeader(identity);
        console.log(identity);
        displayResTypes(identity.reservation_types);
        const resTypeSelect = document.getElementById('res_type');
        resTypeSelect.addEventListener('change', async (e) => {
            payload.reservation_type_id = e.target.value;
            console.log(e.target.value);
            try {
                const themeList = await fetchThemes(e.target.value);
                displayThemes(themeList);

                const themes = document.querySelector('.theme');
                themes.addEventListener('change', (event) => {
                    if (!event.target.matches("input[type='checkbox']")) return;
                
                    const themeId = event.target.value;

                    if (event.target.checked) {
                        payload.themes_id_list.push(themeId);
                    } else {
                        payload.themes_id_list = payload.themes_id_list.filter(
                            id => id !==themeId);
                    }
                    console.log(payload);
                    });
                } catch(error) {
                    alert(error.message);
                }
            });
            console.log(payload);
        } catch(error) {
            alert(error.message);
        }
    });
    try {
        const statuses =  await fetchStatus();
        displayStatus(statuses);
        const statusSelect = document.getElementById('status');
        statusSelect.addEventListener('change', (event) => {
        payload.status_id = event.target.value;
        console.log(payload);
    })
    } catch(error) {
        alert(error.message)
    }
    
    displayStructType(test);
    displayStruct(test);
    
    const structType = document.getElementById('struct_type');
    const structSelect = document.getElementById('struct_name');

    

    

    structSelect.addEventListener('change', (event) => {
        payload.structure_id = event.target.value;
        console.log(payload);
    })

    

function displayResTypes(data) {
    const ResTypeContainer = document.querySelector('.res_type');

    const resTypeField = document.createElement('div');
    resTypeField.classList.add('field');

    const resTypeLabel = document.createElement('label');
    resTypeLabel.setAttribute('for', 'res_Type');
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

function displayStructType(data) {
    const select = document.getElementById('struct_type');
    data.forEach((element) => {
        const option = document.createElement('option');
        option.value = element.id;
        option.textContent = element.name;
        select.appendChild(option);
    })
}

function displayStruct(data) {
    const select = document.getElementById('struct_name');
    data.forEach((element) => {
        const option = document.createElement('option');
        option.value = element.id;
        option.textContent = element.name;
        select.appendChild(option);
    })
}
