from .repository import Repository, db
from app.models.reservation import Reservation


class ReservationRepository(Repository):
    def __init__(self):
        super().__init__(Reservation)
    # l'ORM a besoin d'un modèle objet pour fonctionner
    # c'est ce qu'on a mis dans l'init de Repository
    # Ici, on précise que le modèle sera User

    def user_res_beetween(self, user_id, start_date, end_date):
        return db.session.scalars(
            db.select(self.model).filter(
                self.model.author_id == user_id,
                self.model.reservation_date >= start_date,
                self.model.reservation_date <= end_date
            )).all()
