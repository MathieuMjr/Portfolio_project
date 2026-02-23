import { getCookie } from "./auth.js";
import { API_BASE_URL } from "./config.js";
import { setHeader } from "./header.js";

const token = getCookie('token');
console.log(token);

document.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch('../html/header.html');
    const header_content = await response.text();
    const header = document.querySelector(".navigation");
    header.innerHTML = header_content;

    await setHeader();

    if (!token) {
        window.location.href = '../html/index.html'
    }
    const now = new Date();
    const firstDay = new Date(now.getFullYear(), now.getMonth(), 1);
    console.log(firstDay);
    const lastDay = new Date(now.getFullYear(), now.getMonth() +1, 0);
    const firstDayString = formatDate(firstDay);
    const lastDayString = formatDate(lastDay);
    try {
        const reservations_data = await fetchMonthRes(firstDayString, lastDayString, token);
        display_planning(firstDay, lastDay, reservations_data);
    } catch(error) {
        alert(error.message);
    }

    

})
// ---------------- FONCTIONS ------------------------------------------------
async function fetchMonthRes(firstDay, lastDay, token) {
    const response = await fetch(
        `${API_BASE_URL}/api/reservations/me/reservations?from=${firstDay}&to=${lastDay}`, {
            method: "GET",
            headers: {
                "Content-type": "application/json",
                "Authorization": `Bearer ${token}`
            }
        });
    if (!response.ok) {
        if (response.status === 401) {
            throw new Error("Votre session a expiré, reconnectez-vous");
        } else if (response.status === 404) {
            throw new Error("Le compte utilisateur est inexistant ou désactivé");
        } else {
            throw new Error("Une erreur inconnue s'est produite - contacter administrateur");
        }
    } else {
        return await response.json();
    }
}

function display_planning(firstDay, lastDay, res_data) {

    const MONTHS = ["Janvier", "Février", "Mars", "Avril", "Mai",
        "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre",
        "Décembre"
    ];

    const month_wrapper = document.querySelector(".month-wrapper");
    month_wrapper.querySelector("h1").textContent = MONTHS[firstDay.getMonth()] + " " + firstDay.getFullYear();

    let iterated_day = new Date(firstDay);

    while(iterated_day <= lastDay) {
        const day_string = formatDate(iterated_day);

        const resOfDay = res_data.filter(
            res => res.reservation_date === day_string
        );
        const sortedRes = resOfDay.toSorted(
            (a, b) => a.hour.localeCompare(b.hour)
        );
        
        displayReservationCards(sortedRes, month_wrapper, iterated_day);

        iterated_day = new Date(
            iterated_day.getFullYear(),
            iterated_day.getMonth(),
            iterated_day.getDate() +1)
    }}

function formatDate(date) {
    return date.toISOString().split("T")[0];
}

function displayReservationCards(data, parent_div, dayDate) {
    const DAYS = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"];
    const dayTitle = document.createElement('h2');
    dayTitle.textContent = `${DAYS[dayDate.getDay()]} ${dayDate.getDate()}`;
    parent_div.appendChild(dayTitle);
    const dayPlanning = document.createElement('div');
    dayPlanning.classList.add('day-planning');
    data.forEach((element) => {
        const card = document.createElement('div');
        card.classList.add('day-card');
        const link = document.createElement('a');
        link.href = `reservation.html?id=${element.id}`;
        const pHour = document.createElement('p');
        pHour.classList.add('hour');
        pHour.textContent = element.hour.slice(0, 5);
        link.appendChild(pHour);
        const pTheme = document.createElement('p');
        pTheme.classList.add('theme');
        const themes = element.themes.map(theme => theme.name);
        pTheme.textContent = themes.join('<br>');
        link.appendChild(pTheme);
        const pResType = document.createElement('p');
        pResType.textContent = element.reservation_type.name;
        link.appendChild(pResType);
        const pStruct = document.createElement('p');
        const dpt = element.structure.zip_code.slice(0, 2);
        pStruct.textContent = `${element.structure.name} (${dpt})`;
        link.appendChild(pStruct);
        card.appendChild(link);
        dayPlanning.appendChild(card);
    });
    parent_div.appendChild(dayPlanning);
}