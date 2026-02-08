from .repository import Repository
from app.models.user import User


class UserRepository(Repository):
    def __init__(self):
        super().__init__(User)
    # l'ORM a besoin d'un modèle objet pour fonctionner
    # c'est ce qu'on a mis dans l'init de Repository
    # (self.model = model)
    # Ici, on précise que le modèle sera User
