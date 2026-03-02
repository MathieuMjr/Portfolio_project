import { fetchCurrentUser, getCookie } from "./auth.js";
import { setHeader } from "./header.js";
import { fetchMonthRes } from "./api.js";
import { formatDate} from "./utils.js";

const token = getCookie('token');

document.addEventListener('DOMContentLoaded', async () => {
    if (!token) {
        window.location.href = '../html/index.html'
    }

    const responseHeader = await fetch('../html/header.html');
    const headerContent = await responseHeader.text();
    const header = document.querySelector(".navigation");
    header.innerHTML = headerContent;

    let identity, monthReservations;
    let currentDate = new Date();
    // Required for displayPlanning
    const firstDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);
    const lastDay = new Date(currentDate.getFullYear(), currentDate.getMonth() +1, 0);
    // Required for fetchMontRes
    const firstDayString = formatDate(firstDay);
    const lastDayString = formatDate(lastDay);
    try {
        [identity, monthReservations] = await Promise.all([
            fetchCurrentUser(),
            fetchMonthRes(firstDayString, lastDayString, token),
        ])
    } catch(error) {
        alert(error.message);
        window.location.href = 'index.html'
    }

    if (identity) {
        setHeader(identity);
    }
        
    if (monthReservations) {
        display_planning(firstDay, lastDay, monthReservations);
    }
    
    
// PLANNING NAVIGATION-----------------------------------------------------
    const responsePlanNav = await fetch('../html/planning_nav.html');
    const planNavContent = await responsePlanNav.text();
    const headPlanNav = document.querySelector(".head_planning_nav");
    const footPlanNav = document.querySelector('.foot_planning_nav');
    headPlanNav.innerHTML = planNavContent;
    footPlanNav.innerHTML = planNavContent;

    headPlanNav.querySelector('.prev_nav_button').addEventListener('click', (event) => {
        event.preventDefault();
        currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth() -1, 1);
        renderMonth(currentDate);
    });
    headPlanNav.querySelector('.next_nav_button').addEventListener('click', (event) => {
        event.preventDefault();
        currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth() +1, 1);
        renderMonth(currentDate);
    });
    footPlanNav.querySelector('.prev_nav_button').addEventListener('click', (event) => {
        event.preventDefault();
        currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth() -1, 1);
        renderMonth(currentDate);
    });
    footPlanNav.querySelector('.next_nav_button').addEventListener('click', (event) => {
        event.preventDefault();
        currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth() +1, 1);
        renderMonth(currentDate);
    });
})

// ---------------- FONCTIONS ------------------------------------------------

function display_planning(firstDay, lastDay, res_data) {

    const MONTHS = ["Janvier", "Février", "Mars", "Avril", "Mai",
        "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre",
        "Décembre"
    ];

    const monthWrapper = document.querySelector(".month-wrapper");
    monthWrapper.innerHTML = "";

    const monthTitle = document.createElement("h1");
    monthWrapper.appendChild(monthTitle);
    monthTitle.textContent = MONTHS[firstDay.getMonth()] + " " + firstDay.getFullYear();

    let iterated_day = new Date(firstDay);

    while(iterated_day <= lastDay) {
        const day_string = formatDate(iterated_day);

        const resOfDay = res_data.filter(
            res => res.reservation_date === day_string
        );
        const sortedRes = resOfDay.toSorted(
            (a, b) => a.hour.localeCompare(b.hour)
        );
        
        displayReservationCards(sortedRes, monthWrapper, iterated_day);

        iterated_day = new Date(
            iterated_day.getFullYear(),
            iterated_day.getMonth(),
            iterated_day.getDate() +1)
    }};

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
        pTheme.innerHTML = themes.join('<br>');
        link.appendChild(pTheme);

        const pResType = document.createElement('p');
        pResType.textContent = element.reservation_type.name;
        pResType.classList.add('res_type');
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