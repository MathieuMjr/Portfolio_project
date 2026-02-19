from .repository import Repository, db
from app.models.user import User


class UserRepository(Repository):
    def __init__(self):
        super().__init__(User)
    # l'ORM a besoin d'un modèle objet pour fonctionner
    # c'est ce qu'on a mis dans l'init de Repository
    # (self.model = model)
    # Ici, on précise que le modèle sera User

    def save(self, user):
        """
        Save a change on a user. Designed for password update in user_service.
        The goal is to keep layer responsibilities
        (no hashing in repo, nor in api) and save it on db.

        :param user: Object user
        """
        db.session.commit()
