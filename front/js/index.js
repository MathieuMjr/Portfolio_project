import { getCookie, login } from "./auth.js";

const token = getCookie('token');
console.log(token);

document.addEventListener('DOMContentLoaded', async () => {

    // if (token) {
    //     window.location.href = '../html/planning.html';
    // }

    const loginForm = document.querySelector('.login-form');
    if (loginForm) {console.log('loginForm');}
    const errorParagraph = document.getElementById('error-credentials');

    loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const payload = {
            'email': document.querySelector('input[name=email]').value,
            'password': document.querySelector('input[name=pwd]').value
        }
        try {
            const apiToken = await login(payload);
            document.cookie = "token=" + apiToken.access_token + "; path=/; SameSite=strict";
            window.location.href = '../html/planning.html';
        } catch (error) {
            errorParagraph.textContent = error.message;
        }
    });
});
