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
            throw new Error("Votre session a expiré, veuillez vous reconnecter");
        } else if (response.status === 404) {
            throw new Error("Le compte utilisateur est inexistant ou désactivé");
        } else {
            throw new Error("Erreur lors de la récupération des réservations - contacter administrateur");
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
        if (response.status === 401) {
            throw new Error("Votre session a expiré, veuillez vous reconnecter");
        } else {
            throw new Error(
            "Erreur lors de la récupération des status de réservation - contacter administrateur");
        }
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
            throw new Error("Votre session a expiré, veuillez vous reconnecter");
        } else {
            throw new Error("Erreur lors de la récupération des thèmes - contacter administrateur");
        }
    } else {
        return response.json();
    }
}

export async function fetchAudienceTypes() {
    const token = getCookie("token");
    const response = await fetch(`${API_BASE_URL}/api/audience_types/`, {
        method: "GET",
        headers: {
            "Content-type": "application/json",
            "Authorization": `Bearer ${token}`
        }
    });
    if (!response.ok) {
        if (response.status === 401) {
            throw new Error("Votre session a expiré, veuillez vous reconnecter");
        } else {
            throw new Error(
                "Erreur lors de la récupération des types d'audience - contacter Admin");
        }
    } else {
        return response.json();
    }
}

export async function fetchStructureTypes() {
    const token = getCookie("token");
    const response = await fetch(`${API_BASE_URL}/api/struct_types/`, {
        method: "GET",
        headers: {
            "Content-type": "application/json",
            "Authorization": `Bearer ${token}`
        }
    });
    if (!response.ok) {
        if (response.status === 401) {
            throw new Error("Votre session a expiré, veuillez vous reconnecter");
        } else {
            throw new Error(
                "Erreur lors de la récupération des types de structure - contacter Admin");
        }
    } else {
        return response.json();
    }
}

export async function fetchStructures(strucT_id, zipCode) {
    if ((!strucT_id) || (!zipCode)) {
        return null;
    } else {
        const token = getCookie("token");
        const response = await fetch(
            `${API_BASE_URL}/api/structures/?type_id=${strucT_id}&zip=${zipCode}`, {
            method: "GET",
            headers: {
            "Content-type": "application/json",
            "Authorization": `Bearer ${token}`
            }
        });
        if (!response.ok) {
            if (response.status === 401) {
            throw new Error("Votre session a expiré, veuillez vous reconnecter");
            } else {
                throw new Error(
                    "Erreur lors de la récupération des structures - contacter Admin");
            }
        } else {
            return response.json();
        }
    }
}

export async function postReservation(payload) {
    const token = getCookie("token");
    const response = await fetch(`${API_BASE_URL}/api/reservations/`, {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify(payload)
    });
    if (!response.ok) {
        if (response.status === 401) {
            throw new Error("Votre session a expiré, veuillez vous reconnecter");
        } else if (response.status === 400) {
            throw new Error('Un champs incorrect a été saisi');
        } else {
            throw new Error('Une erreur est survenue');
        }
    } else {
        return await response.json();
    }
}

export async function fetchReservation(reservationId) {
    const token = getCookie("token");
    const response = await fetch(`${API_BASE_URL}/api/reservations/${reservationId}`, {
        method: "GET",
        headers: {
            "Content-type": "application/json",
            "Authorization": `Bearer ${token}`
        }
    });
    if (!response.ok) {
        if (response.status === 401) {
            throw new Error("Votre session a expiré, veuillez vous reconnecter");
        } else {
            throw new Error(
                "Erreur lors de la récupération de la réservation - contacter Admin");
        }
    } else {
        return response.json();
    }
}

export async function putReservation(payload, reservationId) {
    const token = getCookie("token");
    const response = await fetch(`${API_BASE_URL}/api/reservations/${reservationId}`, {
        method: "PUT",
        headers: {
            "Content-type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify(payload)
    });
    if (!response.ok) {
        if (response.status === 401) {
            throw new Error("Votre session a expiré, veuillez vous reconnecter");
        } else if (response.status === 400) {
            // A revoir !
            const errorMessage = await response.json()
            throw new Error(errorMessage.error);
        } else if (response.status === 404) {
            throw new Error("Ressource introuvable (réservation, status, theme ou audiences)")
        } else {
            throw new Error(error.message);
        }
    } else {
        return await response.json();
    }
}