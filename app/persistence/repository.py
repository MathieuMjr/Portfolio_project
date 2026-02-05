from app.extensions import db


class Repository:
    def __init__(self, model):
        self.model = model

    def get_id(self, id):
        return db.get_or_404(self.model, id)

    def get_all(self):
        return db.session.scalars(db.select(self.model)).all()

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def update(self, obj_id, data):
        obj = self.get_id(obj_id)
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        # if 'password' in data:
            # hashing
        db.session.commit()

    def delete(self, obj_id):
        return self.update(obj_id, {"is_active": False})

    def get_by_attribute(self, attribute_name, attribute_value):
        if not hasattr(self.model, attribute_name):
            return []
        return db.session.scalars(
            db.select(self.model).where(
                getattr(self.model, attribute_name) == attribute_value
            )
        ).all()
