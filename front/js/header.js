export async function setHeader(identity) {
    const firstname = document.getElementById('firstname');
    const lastname = document.getElementById('lastname');
    firstname.textContent = identity.firstname;
    lastname.textContent = identity.lastname;
}