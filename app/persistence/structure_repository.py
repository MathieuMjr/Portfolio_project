from .repository import Repository, db
from app.models.structure import Structure


class StructureRepository(Repository):
    def __init__(self):
        super().__init__(Structure)
    # l'ORM a besoin d'un modèle objet pour fonctionner
    # c'est ce qu'on a mis dans l'init de Repository
    # Ici, on précise que le modèle sera User

    def structure_by_type_and_zip(self, structT_id, zip_code):
        """
        Query the db to retrieve a list of structure of a given
        structure type and with a specific zip code.
        """
        return db.session.scalars(
            db.select(self.model).filter(
                self.model.zip_code == zip_code,
                self.model.structure_type_id == structT_id
            )
        ).all()
