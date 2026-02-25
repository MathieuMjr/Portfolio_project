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
    "themes_id_list": [null],
    "audiences": [null]
};


document.addEventListener('DOMContentLoaded', () => {
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

    displayResTypes(test);
    displayStatus(test);

    const resTypeSelect = document.getElementById('res_type');
    const statusSelect = document.getElementById('status');
    resTypeSelect.addEventListener('change', (e) => {
        payload.reservation_type_id = e.target.value;
        console.log(payload);
    })

    statusSelect.addEventListener('change', (event) => {
        payload.status_id = event.target.value;
        console.log(payload);
    })

});

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

async function fetchUserResType() {
    
}