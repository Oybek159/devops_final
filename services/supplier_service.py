
from database.models import Supplier
from database.db import db

class SupplierService:

    @staticmethod
    def create_supplier(company, service):
        supplier = Supplier(company=company, service=service)
        db.session.add(supplier)
        db.session.commit()
        return supplier

    @staticmethod
    def get_all():
        return Supplier.query.all()

    @staticmethod
    def get_by_id(id):
        return Supplier.query.get(id)

    @staticmethod
    def update_supplier(id, company, service):
        supplier = Supplier.query.get(id)
        if supplier:
            supplier.company = company
            supplier.service = service
            db.session.commit()
            return supplier
        return None

    @staticmethod
    def delete_supplier(id):
        supplier = Supplier.query.get(id)
        if supplier:
            db.session.delete(supplier)
            db.session.commit()
            return True
        return False
