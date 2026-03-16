import { fetchCurrentUser, getCookie } from "./auth.js";
import { setHeader } from "./header.js";
import { fetchMonthRes, fetchUsers } from "./api.js";
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

    try {
        identity = await fetchCurrentUser()
    } catch(error) {
        alert(error.message);
        window.location.href = 'index.html'
    }

    let usersList;

    if (identity) {
        setHeader(identity);
        if (identity.role) {
            try {
                usersList = await fetchUsers();
                displayUsersSelect(identity.role, usersList);
            } catch(error) {
                alert(error.message);
            }
        }
        try {
            monthReservations = await navigateToMonth(currentDate, identity.id);
        } catch(error) {
            alert(error.message);
        }
    }

    document.getElementById("logout").addEventListener("click", () => {
    document.cookie = "token=; Max-Age=0; path=/";
    window.location.href = "../html/index.html";
    });

    if (document.getElementById("usersList")) {
            document.getElementById("usersList").addEventListener('change', async (e) => {
                try {
                    identity.id = e.target.value;
                    const userMonthReservations  = await navigateToMonth(currentDate, identity.id);
                } catch(error) {
                    alert(error.message)
                }
            })
        }
    
    
// PLANNING NAVIGATION-----------------------------------------------------
    const responsePlanNav = await fetch('../html/planning_nav.html');
    const planNavContent = await responsePlanNav.text();
    const headPlanNav = document.querySelector(".head_planning_nav");
    const footPlanNav = document.querySelector('.foot_planning_nav');
    headPlanNav.innerHTML = planNavContent;
    footPlanNav.innerHTML = planNavContent;

    headPlanNav.querySelector('.prev_nav_button').addEventListener('click', async (event) => {
    event.preventDefault();
    currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1);
    await navigateToMonth(currentDate, identity.id);
})

    headPlanNav.querySelector('.next_nav_button').addEventListener('click', async (event) => {
    event.preventDefault();
    currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1);
    await navigateToMonth(currentDate, identity.id);
})

    footPlanNav.querySelector('.prev_nav_button').addEventListener('click', async (event) => {
    event.preventDefault();
    currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1);
    await navigateToMonth(currentDate, identity.id);
})

    footPlanNav.querySelector('.next_nav_button').addEventListener('click', async (event) => {
    event.preventDefault();
    currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1);
    await navigateToMonth(currentDate, identity.id);
})
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
        pStruct.classList.add('struct');
        const dpt = element.structure.zip_code.slice(0, 2);
        pStruct.textContent = `${element.structure.name} (${dpt})`;
        link.appendChild(pStruct);

        card.appendChild(link);

        dayPlanning.appendChild(card);
    });
    parent_div.appendChild(dayPlanning);
}

async function navigateToMonth(date, userId) {
    const firstDay = new Date(date.getFullYear(), date.getMonth(), 1);
    const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
    const monthReservations = await fetchMonthRes(formatDate(firstDay), formatDate(lastDay), token, userId);
     console.log("RESERVATIONS:", monthReservations);
    if (monthReservations) display_planning(firstDay, lastDay, monthReservations);
}

function displayUsersSelect(role, usersList) {
        if (role && usersList) {
            const userListDiv = document.getElementById('users_select');
            const userListLabel = document.createElement('label');
            userListLabel.setAttribute('for', 'usersList');
            userListDiv.append(userListLabel);

            const userListSelect = document.createElement('select');
            userListSelect.id='usersList';
            userListSelect.name='usersList';

            const defaultOption = document.createElement('option');
            defaultOption.value = "";
            defaultOption.textContent = "Planning utilisateur";
            userListSelect.appendChild(defaultOption);

            usersList.forEach((user) => {
                const option = document.createElement('option');
                option.value = user.id;
                option.innerText = `${user.firstname} ${user.lastname}`;
                userListSelect.appendChild(option);
            })
            userListDiv.appendChild(userListSelect);
    }
}