from dotenv import load_dotenv
from app import create_app
from app.extensions import db
from app.models.reservation_type import ReservationType
from app.models.user import User
from app.persistence.user_repository import UserRepository
from app.persistence.reservation_type_repository import (
    ReservationTypeRepository)

load_dotenv()

app = create_app()


def create_reservation_types():
    resT_repo = ReservationTypeRepository()

    res_types_data = [
        {'name': 'Animation'},
        {'name': 'Exposition panneaux'},
        {'name': "Visite d'exposition"},
        {'name': "Location d'expo volumes"}
    ]
    for data in res_types_data:
        rs = resT_repo.get_by_attribute('name', data['name'])
        if len(rs) == 0:
            new_rs = ReservationType(**data)
            resT_repo.add(new_rs)
            print('Reservation type created:')
            print(new_rs.to_dict())
        else:
            print('Reservation type already exist:')
            print(f'{rs[0].name}: {rs[0].id}')


def create_default_admin():
    user_repo = UserRepository()
    data = {
        'firstname': 'Admin',
        'lastname': 'admin',
        'email': 'admin@kotools.fr',
        'password': '12345',
        'role': True
        }
    check_admin = user_repo.get_by_attribute('email', data['email'])
    if len(check_admin) == 0:
        admin = User(**data)
        user_repo.add(admin)
        print(f'Admin created : {admin.id}')
    else:
        print(f'Admin already exist: {check_admin[0].id}')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_reservation_types()
        create_default_admin()
    app.run()
