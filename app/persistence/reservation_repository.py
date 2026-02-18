from .repository import Repository, db
from app.models.reservation import Reservation


class ReservationRepository(Repository):
    def __init__(self):
        super().__init__(Reservation)
    # l'ORM a besoin d'un modèle objet pour fonctionner
    # c'est ce qu'on a mis dans l'init de Repository
    # Ici, on précise que le modèle sera User

    def user_res_beetween(self, user_id, start_date, end_date):
        """
        Query the db to retrieve user's reservation in
        a date interval (pagination)

        :param user_id: ID of the user
        :param start_date: Start of the date interval (included)
        :param end_date: End of the date interval (included)
        """
        return db.session.scalars(
            db.select(self.model).filter(
                self.model.author_id == user_id,
                self.model.reservation_date >= start_date,
                self.model.reservation_date <= end_date
            )).all()
