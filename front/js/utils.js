export function formatDate(date) {
    // return date.toISOString().split("T")[0];
    return date.toLocaleDateString('fr-CA');
}