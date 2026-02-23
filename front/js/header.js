import { fetchCurrentUser } from "./auth.js";
import { getCookie } from "./auth.js";

export async function setHeader() {
    try {
        const identity = await fetchCurrentUser();
        const firstname = document.getElementById('firstname');
        const lastname = document.getElementById('lastname');
        firstname.textContent = identity.firstname;
        lastname.textContent = identity.lastname;
    } catch (error) {
        alert(error.message);
    }
}