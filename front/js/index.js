import { getCookie, login } from "./auth.js";


document.addEventListener('DOMContentLoaded', async () => {

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
            window.location.href = '../html/planning.html';
        } catch (error) {
            errorParagraph.textContent = error.message;
        }
    });
});
