from database.db import db

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    product = db.Column(db.String(120))

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(120))
    service = db.Column(db.String(150))

class Procurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer)
    supplier_id = db.Column(db.Integer)
    status = db.Column(db.String(50))
