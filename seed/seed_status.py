from app.models.status import Status
from app.persistence.status_repository import StatusRepository


def create_status():
    status_repos = StatusRepository()
    data = [
        {'name': "En attente d'informations"},
        {'name': "En signature structure"},
        {'name': "En signature direction"},
        {'name': "Reservée"},
        {'name': "A facturer"},
        {'name': "Réservation close"},
        {'name': "Annulée"}
    ]
    for element in data:
        check_status = status_repos.get_by_attribute('name', element['name'])
        if len(check_status) == 0:
            status = Status(**element)
            status_repos.add(status)
