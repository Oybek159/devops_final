from flask import Blueprint, request, jsonify
from database.models import Supplier
from database.db import db

supplier_bp = Blueprint("suppliers", __name__)

@supplier_bp.route("/add", methods=["POST"])
def add_supplier():
    """
    Create a new supplier
    ---
    tags:
      - Suppliers
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - company
            - service
          properties:
            company:
              type: string
            service:
              type: string
    responses:
      201:
        description: Supplier added
    """
    data = request.json
    s = Supplier(company=data['company'], service=data['service'])
    db.session.add(s)
    db.session.commit()
    return jsonify({"message": "Supplier added"}), 201


@supplier_bp.route("/", methods=["GET"])
def get_suppliers():
    """
    Get all suppliers
    ---
    tags:
      - Suppliers
    responses:
      200:
        description: List of suppliers
    """
    suppliers = Supplier.query.all()
    return jsonify([{"id": s.id, "company": s.company, "service": s.service} for s in suppliers])


@supplier_bp.route("/<int:id>", methods=["GET"])
def get_supplier(id):
    """
    Get supplier by ID
    ---
    tags:
      - Suppliers
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Supplier found
      404:
        description: Supplier not found
    """
    s = Supplier.query.get(id)
    if not s:
        return jsonify({"error": "Supplier not found"}), 404
    return jsonify({"id": s.id, "company": s.company, "service": s.service})


@supplier_bp.route("/update/<int:id>", methods=["PUT"])
def update_supplier(id):
    """
    Update supplier
    ---
    tags:
      - Suppliers
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            company:
              type: string
            service:
              type: string
    responses:
      200:
        description: Supplier updated
      404:
        description: Supplier not found
    """
    s = Supplier.query.get(id)
    if not s:
        return jsonify({"error": "Supplier not found"}), 404
    data = request.json
    s.company = data["company"]
    s.service = data["service"]
    db.session.commit()
    return jsonify({"message": "Supplier updated"})


@supplier_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_supplier(id):
    """
    Delete supplier
    ---
    tags:
      - Suppliers
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Supplier deleted
      404:
        description: Supplier not found
    """
    s = Supplier.query.get(id)
    if not s:
        return jsonify({"error": "Supplier not found"}), 404
    db.session.delete(s)
    db.session.commit()
    return jsonify({"message": "Supplier deleted"})
