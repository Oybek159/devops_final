from database.models import Farmer
from database.db import db

class FarmerService:

    @staticmethod
    def create_farmer(name, product):
        farmer = Farmer(name=name, product=product)
        db.session.add(farmer)
        db.session.commit()
        return farmer

    @staticmethod
    def get_all():
        return Farmer.query.all()

    @staticmethod
    def get_by_id(id):
        return Farmer.query.get(id)

    @staticmethod
    def update_farmer(id, name, product):
        farmer = Farmer.query.get(id)
        if farmer:
            farmer.name = name
            farmer.product = product
            db.session.commit()
            return farmer
        return None

    @staticmethod
    def delete_farmer(id):
        farmer = Farmer.query.get(id)
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
