import { API_BASE_URL } from "./config.js";

export function getCookie(cookie_name) {
    const decoded = decodeURIComponent(document.cookie);
    const decoded_array = decoded.split(';');
    for (const item of decoded_array) {
        const [key, value] = item.split('=');
        if (key === cookie_name) {
            return value
        }
    }
    return null;
}

export async function login(payload) {
    const response = await fetch(`${API_BASE_URL}/api/login/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    });
    if (!response.ok) {
        const error = await response.json();
        if (response.status === 404) {
            throw new Error(error.message || 'Identifiants invalides');
        } else if (response.status === 500) {
            throw new Error(error.message || 'Erreur serveur - contacter adminstrateur');
        } else {
            throw new Error(error.message || 'Une erreur est survenue');
        }
        } else {
            return await response.json();
        }
    }