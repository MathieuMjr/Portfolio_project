from app.extensions import db


class Repository:
    def __init__(self, model):
        self.model = model

    def get_id(self, id):
        """
        Retrieve an entity with its ID.
        Becarefull, object "is_active": False are retrieved too.

        :param id: Entity id
        """
        return db.session.get(self.model, id)

    def get_all(self, include_inactive=False):
        """
        Retrieve all active entities of a repository.
        Include_inactive specify to add or not entities with "is_active": False

        :param include_inactive: True if "is_active": False are wanted
        """
        if not include_inactive:
            return db.session.scalars(
                db.select(self.model)
                .filter_by(is_active=True)
                .order_by(self.model.creation_date)
                ).all()
        return db.session.scalars(
            db.select(self.model)
            .order_by(self.model.creation_date)
        ).all()

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def update(self, obj, data):
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        db.session.commit()
        # doit recevoir un objet et pas un id
        # le service peut ainsi get_id, vérifier is_active
        # décider s'il fait 404 car is_active False, ou s'il
        # appelle update

    def delete(self, obj):
        """
        Method to soft delete an entity.

        :param obj: Entity to soft delete
        """
        return self.update(obj, {"is_active": False})

    def get_by_attribute(self, attribute_name, attribute_value):
        if not hasattr(self.model, attribute_name):
            return []
        return db.session.scalars(
            db.select(self.model).where(
                getattr(self.model, attribute_name) == attribute_value
            )
        ).all()

    def get_all_deleted(self):
        """
        Retrieve only entities with field
        "is_active": False

        """
        return db.session.scalars(
            db.select(self.model).filter_by(
                is_active=False)).all()
        # Ne renvoie que les inactifs
