from app.extensions import db


class Repository:
    def __init__(self, model):
        self.model = model

    def get_id(self, id):
        return db.get_or_404(self.model, id)
        # Le service fera 404 si is_active:false

    def get_all(self, include_inactive=False):
        if not include_inactive:
            return db.session.scalars(
                db.select(self.model).filter_by(
                    is_active=True)).all()
        return db.session.scalars(db.select(self.model)).all()
        # prend un paramètre pour savoir si doit afficher les
        # is_active False

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def update(self, obj, data):
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        # if 'password' in data:
            # hashing
        db.session.commit()
        # doit recevoir un objet et pas un id
        # le service peut ainsi get_id, vérifier is_active
        # décider s'il fait 404 car is_active False, ou s'il
        # appelle update

    def delete(self, obj):
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
        return db.session.scalars(
            db.select(self.model).filter_by(
                is_active=False)).all()
        # Ne renvoie que les inactifs
