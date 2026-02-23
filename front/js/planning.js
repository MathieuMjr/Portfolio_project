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
        display_planning(reservations_data, firstDay, lastDayString);

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

function display_planning(data, firstDay, lastDay) {

    const MONTHS = ["Janvier", "Février", "Mars", "Avril", "Mai",
        "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre",
        "Décembre"
    ];

    const month_wrapper = document.querySelector(".month-wrapper");
    month_wrapper.querySelector("h1").textContent = MONTHS[firstDay.getMonth()] + " " + firstDay.getFullYear();
        

    }

function formatDate(date) {
    return date.toISOString().split("T")[0];
}