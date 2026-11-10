import { API_BASE_URL } from "./config.js";
import { getCookie } from "./auth.js";

// Fetch reservation of a specific month
export async function fetchMonthRes(firstDay, lastDay, user_id) {
    // console.log('fetch month triggered')
    const response = await fetch(
        `${API_BASE_URL}/api/reservations/${user_id}/reservations?from=${firstDay}&to=${lastDay}`, {
            method: "GET",
            credentials: "include",
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

// Fetch the list of existing statuses
export async function fetchStatus() {
    const response = await fetch(`${API_BASE_URL}/api/statuses/`, {
        method: "GET",
        credentials: "include",
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

// Fetch the list of existing themes
export async function fetchThemes(resTypeId) {
    const response = await fetch(
        `${API_BASE_URL}/api/res_types/${resTypeId}/themes`, {
            method: "GET",
            credentials: "include",
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

// Fetch the list of existing audience types
export async function fetchAudienceTypes() {
    const response = await fetch(`${API_BASE_URL}/api/audience_types/`, {
        method: "GET",
        credentials: "include",
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

// Fetch the list of existing structure types
export async function fetchStructureTypes() {
    const response = await fetch(`${API_BASE_URL}/api/struct_types/`, {
        method: "GET",
        credentials: "include",
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

// Fetch the list of existing structures for a given structure type and zip code
export async function fetchStructures(strucT_id, zipCode) {
    if ((!strucT_id) || (!zipCode)) {
        return null;
    } else {
        const response = await fetch(
            `${API_BASE_URL}/api/structures/?type_id=${strucT_id}&zip=${zipCode}`, {
            method: "GET",
            credentials: "include",
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

// Send a payload to create a new reservation
export async function postReservation(payload) {
    const response = await fetch(`${API_BASE_URL}/api/reservations/`, {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRF-TOKEN": getCookie("csrf_access_token"),
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

// Fetch a specific reservation detail
export async function fetchReservation(reservationId) {
    const response = await fetch(`${API_BASE_URL}/api/reservations/${reservationId}`, {
        method: "GET",
        credentials: "include",
        headers: {
            "X-CSRF-TOKEN": getCookie("csrf_access_token"),
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

// Update a specific reservation
export async function putReservation(payload, reservationId) {
    const response = await fetch(`${API_BASE_URL}/api/reservations/${reservationId}`, {
        method: "PUT",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRF-TOKEN": getCookie("csrf_access_token"),
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

// Fetch the list of existing users
export async function fetchUsers() {
    const response = await fetch(`${API_BASE_URL}/api/users/`, {
        method: "GET",
        credentials: "include",
        headers: {
            "X-CSRF-TOKEN": getCookie("csrf_access_token"),
        }
    });
    if (!response.ok) {
        if (response.status === 401) {
            throw new Error("Votre session a expiré, veuillez vous reconnecter");
        } else if (response.status === 403) {
            throw new Error("Accès refusé");
        } else {
            throw new Error(error.message);
        }
    } else {
        return await response.json();
    } 
}