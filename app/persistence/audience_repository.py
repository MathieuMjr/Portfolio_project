from .repository import Repository, db
from app.models.audience import Audience


class AudienceRepository(Repository):
    def __init__(self):
        super().__init__(Audience)
    # l'ORM a besoin d'un modèle objet pour fonctionner
    # c'est ce qu'on a mis dans l'init de Repository
    # Ici, on précise que le modèle sera User

    def hard_delete(self, obj):
        """
        This method should be used only when updating
        audiences from a reservation udpate to delete
        previous audiences before creating new ones.

        :param self:
        :param obj: Audience to delete
        """
        db.session.delete(obj)
        db.session.commit()
