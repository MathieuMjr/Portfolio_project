from app.persistence.reservation_type_repository import (
    ReservationTypeRepository)
from app.models.reservation_type import ReservationType
from app.models.theme import Theme
from app.persistence.theme_repository import ThemeRepository


def create_reservation_types_and_themes():
    resT_repo = ReservationTypeRepository()
    theme_repo = ThemeRepository()

    res_types_data = [
        {'name': 'Animation'},
        {'name': 'Exposition panneaux'},
        {'name': "Visite d'exposition"},
        {'name': "Location d'expo volumes"}
    ]

    themes = {
        "Animation": [
            {'name': 'Retour vers la Préhistoire'},
            {'name': 'Fée éléctricité'},
            {'name': 'Les métamorphoses du lait'}
        ],
        "Exposition panneaux": [
            {'name': 'Découvreuses anonymes'},
            {'name': 'Pasteur au service de la Science'},
            {'name': 'A la lumière des lasers'}
        ],
        "Location d'expo volumes": [
            {'name': 'Mission corps humain'},
            {'name': "Oups ! Au coeur de l'erreur"},
            {'name': "En avant Mars"}
        ],
        "Visite d'exposition": [
            {'name': "L'île de la découverte"},
            {'name': "Voyage en nord"},
            {'name': "Touche à tout"}
        ]
    }

    res_types_ids = []
    for data in res_types_data:
        rs = resT_repo.get_by_attribute('name', data['name'])
        if len(rs) == 0:
            new_rs = ReservationType(**data)
            resT_repo.add(new_rs)
            res_types_ids.append(new_rs.id)
            for element in themes[new_rs.name]:
                theme_check = theme_repo.get_by_attribute(
                    'name', element['name'])
                if len(theme_check) == 0:
                    element['reservation_type_id'] = new_rs.id
                    theme = Theme(**element)
                    theme_repo.add(theme)
    if len(res_types_ids) != 0:
        check = resT_repo.get_id(res_types_ids[-1])
        resT_repo.delete(check)
