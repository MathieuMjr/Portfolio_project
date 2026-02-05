from .repository import Repository
from app.models.audience_type import AudienceType


class AudienceTypeRepository(Repository):
    def __init__(self):
        super().__init__(AudienceType)
    # l'ORM a besoin d'un modèle objet pour fonctionner
    # c'est ce qu'on a mis dans l'init de Repository
    # Ici, on précise que le modèle sera User
