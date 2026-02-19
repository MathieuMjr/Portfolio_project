from app.models.user import User
from app.persistence.user_repository import UserRepository


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
        admin.hash_pwd(admin.password)
        user_repo.add(admin)
