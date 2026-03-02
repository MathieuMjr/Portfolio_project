import { fetchThemes } from "./api.js";

// --- DISPLAY FUNCTIONS ---------------------------------------------------   
export function displayStructDetails(address, town, email, phone) {
    const addressInput = document.getElementById('struct_address');
    const townInput = document.getElementById('struct_town');
    const emailInput = document.getElementById('struct_mail');
    const phoneInput = document.getElementById('struct_tel');

    addressInput.value = address;
    townInput.value = town;
    emailInput.value = email;
    phoneInput.value = phone;
}
// -- RESERVATION TYPES
export function displayResTypes(data) {
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
export function displayStatus(data) {
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
export function displayThemes(data) {
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
export function displayStructType(data) {
    const select = document.getElementById('struct_type');
    data.forEach((element) => {
        const option = document.createElement('option');
        option.value = element.id;
        option.textContent = element.name;
        select.appendChild(option);
    })
}

// STRUCTURES
export function displayStructNames(data) {
    const select = document.getElementById('struct_name');
    select.innerHTML = "";
    const defaultOption = document.createElement('option');
    defaultOption.value = "";
    defaultOption.textContent = "Veuillez choisir une option";
    select.appendChild(defaultOption);
    data.forEach((element) => {
        const option = document.createElement('option');
        option.value = element.id;
        option.textContent = element.name;
        option.dataset.address = element.address;
        option.dataset.town = element.town;
        option.dataset.phone = element.phone;
        option.dataset.email = element.email;
        select.appendChild(option);
    })
}

// -- AUDIENCE TYPES
export function displayAudienceTypes(data) {
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

export async function displayExistingRes(resDetails) {
    const select = document.getElementById('struct_name');
    select.disabled = true;
    const option = document.createElement('option');
    option.value = resDetails.structure.id;
    option.textContent = resDetails.structure.name;
    select.appendChild(option);
    select.value = resDetails.structure.id;
    document.getElementById('struct_town').value = resDetails.structure.town;
    document.getElementById('struct_address').value = resDetails.structure.address;
    document.getElementById('struct_mail').value = resDetails.structure.email;
    document.getElementById('struct_tel').value = resDetails.structure.phone;
    document.getElementById('struct_type').disabled = true;
    document.getElementById('struct_type').value = resDetails.structure.structure_type.id;
    document.getElementById('struct_zip').disabled = true;
    document.getElementById('struct_zip').value = resDetails.structure.zip_code;
    document.getElementById('contact_firstname').value = resDetails.contact.firstname;
    document.getElementById('contact_lastname').value = resDetails.contact.lastname;
    document.getElementById('contact_email').value = resDetails.contact.email;
    document.getElementById('contact_phone').value = resDetails.contact.phone;
    document.getElementById('contact_role').value = resDetails.contact.role;
    resDetails.audiences.forEach((audience) => {
        document.getElementById(audience.audience_type.name).value = audience.count;
    });
    document.getElementById('price').value = resDetails.price;
    document.getElementById('reservation_date').value = resDetails.reservation_date;
    document.getElementById('hour').value = resDetails.hour;
    document.getElementById('status').value = resDetails.status.id;
    document.getElementById('res_type').value = resDetails.reservation_type.id;
    document.getElementById('res_type').disabled = true;
    const themeList = await fetchThemes(resDetails.reservation_type.id);
    if (themeList) {
        console.log(themeList);
        displayThemes(themeList);
    }
    resDetails.themes.forEach((theme) => {
        document.getElementById(`theme_${theme.id}`).checked = true;
    });
}
