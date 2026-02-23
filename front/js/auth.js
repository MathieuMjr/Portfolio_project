import { API_BASE_URL } from "./config.js";

// --- GET COOKIE BY NAME -------------------------------------------
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

// --- LOGIN -------------------------------------------------------
export async function login(payload) {
    const response = await fetch(`${API_BASE_URL}/api/login/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    });
    if (!response.ok) {
        if (response.status === 401) {
            throw new Error('Identifiants invalides');
        } else if (response.status === 500) {
            throw new Error('Erreur serveur - contacter adminstrateur');
        } else {
            throw new Error('Une erreur est survenue');
        }
        } else {
            return await response.json();
        }
    }

// --- FETCH CURRENT USER ------------------------------------------
    export async function fetchCurrentUser() {
    const token = getCookie("token");
    const response = await fetch(`${API_BASE_URL}/api/users/me`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    })
    if (!response.ok) {
        if (response.status === 404) {
            throw new Error("Utilisateur introuvable ou désactivé");
        } else if (response.status === 500) {
            throw new Error("Le serveur a rencontré un problème - contacter administrateur");
        } else if (response.status === 401) {
            throw new Error("Votre session a expiré, veuillez vous reconnecter");
        } else {
            throw new Error("Une erreur inconnue est survenue - contacter administrateur");
        }
    }
    return await response.json();
}