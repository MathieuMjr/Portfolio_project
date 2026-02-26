import { API_BASE_URL } from "./config.js";
import { getCookie } from "./auth.js";

export async function fetchMonthRes(firstDay, lastDay, token) {
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

export async function fetchStatus() {
    const token = getCookie("token");
    const response = await fetch(`${API_BASE_URL}/api/statuses/`, {
        method: "GET",
        headers: {
                "Content-type": "application/json",
                "Authorization": `Bearer ${token}`
            }
        });
    if (!response.ok) {
        throw new Error("Une erreur inconnue s'est produite - contacter administrateur");
    } else {
        return response.json();
    }
}

export async function fetchThemes(resTypeId) {
    const token = getCookie("token");
    const response = await fetch(
        `${API_BASE_URL}/api/res_types/${resTypeId}/themes`, {
            method: "GET",
            headers: {
                "Content-type": "application/json",
                "Authorization": `Bearer ${token}`
            }
        });
    if (!response.ok) {
        if (response.status === 400) {
            throw new Error("Le type de réservation fourni n'a pas été trouvé");
        } else if (response.status === 401) {
            throw new Error("Votre session a expiré, reconnectez-vous");
        } else {
            throw new Error("Une erreur inconnue s'est produite - contacter administrateur");
        }
    } else {
        return response.json();
    }
}