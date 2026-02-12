from dotenv import load_dotenv
import json
from app import create_app, db
from seed.seed_admin import create_default_admin
from seed.seed_audience_types import create_audience_types
from seed.seed_res_types_theme import create_reservation_types_and_themes
from seed.seed_status import create_status
from seed.seed_struct_types import create_structure_types
from app.persistence.status_repository import StatusRepository
from app.persistence.structure_type_repository import StructureTypeRepository
from app.persistence.audience_type_repository import AudienceTypeRepository
from app.persistence.theme_repository import ThemeRepository
from app.persistence.reservation_type_repository import (
    ReservationTypeRepository
)
from app.persistence.user_repository import UserRepository

load_dotenv()

app = create_app()


def export():
    resT_repo = ReservationTypeRepository()
    status_repo = StatusRepository()
    theme_repo = ThemeRepository()
    structT_repo = StructureTypeRepository()
    audT_repo = AudienceTypeRepository()
    user_repo = UserRepository()

    values = []

    resT = [{"key": element.name,
             "value": element.id,
             "type": "default",
             "enabled": True} for element in resT_repo.get_all(
                 include_inactive=True)]
    status = [{"key": element.name,
               "value": element.id,
               "type": "default",
               "enabled": True} for element in status_repo.get_all(
                 include_inactive=True)]
    theme = [{"key": element.name,
              "value": element.id,
              "type": "default",
              "enabled": True} for element in theme_repo.get_all(
                 include_inactive=True)]
    structT = [{"key": element.name,
                "value": element.id,
                "type": "default",
                "enabled": True} for element in structT_repo.get_all(
                    include_inactive=True)]
    audT = [{"key": element.name,
             "value": element.id,
             "type": "default",
             "enabled": True} for element in audT_repo.get_all(
                 include_inactive=True)]
    user = [{"key": element.firstname,
             "value": element.id,
             "type": "default",
             "enabled": True} for element in user_repo.get_all(
                 include_inactive=True)]

    values.extend(resT)
    values.extend(status)
    values.extend(theme)
    values.extend(structT)
    values.extend(audT)
    values.extend(user)

    data = {
        "id": "0272023d-7cbc-492e-8aff-bb990d6352bb",
        "name": "Ko.tools_env",
        "values": values
    }

    with open('exports/env.json', "w") as f:
        json.dump(data, f, indent=4)


def run_seed():
    with app.app_context():
        db.create_all()
        create_audience_types()
        create_reservation_types_and_themes()
        create_status()
        create_default_admin()
        create_structure_types()
        create_status()
        export()


if __name__ == '__main__':
    run_seed()

# pytho-m seed.seed_db dans mathieu@Mathieu:~/my_repos/Portfolio_project$
