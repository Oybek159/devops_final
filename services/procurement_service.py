from database.models import Procurement
from database.db import db

class ProcurementService:

    @staticmethod
    def create_order(farmer_id, supplier_id):
        order = Procurement(
            farmer_id=farmer_id,
            supplier_id=supplier_id,
            status="Pending"
        )
        db.session.add(order)
        db.session.commit()
        return order

    @staticmethod
    def get_all():
        return Procurement.query.all()

    @staticmethod
    def update_status(id, status):
        order = Procurement.query.get(id)
        if order:
            order.status = status
            db.session.commit()
            return order
        return None

    @staticmethod
    def delete_order(id):
        order = Procurement.query.get(id)
        if order:
            db.session.delete(order)
            db.session.commit()
            return True
        return False
