from flask import Blueprint, request, jsonify
from database.models import Farmer
from database.db import db

farmer_bp = Blueprint("farmers", __name__)

@farmer_bp.route("/add", methods=["POST"])
def add_farmer():
    """
    Create a new farmer
    ---
    tags:
      - Farmers
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - name
            - product
          properties:
            name:
              type: string
            product:
              type: string
    responses:
      201:
        description: Farmer added successfully
    """
    data = request.json
    farmer = Farmer(name=data['name'], product=data['product'])
    db.session.add(farmer)
    db.session.commit()
    return jsonify({"message": "Farmer added"}), 201


@farmer_bp.route("/", methods=["GET"])
def get_all_farmers():
    """
    Get all farmers
    ---
    tags:
      - Farmers
    responses:
      200:
        description: List of all farmers
    """
    farmers = Farmer.query.all()
    return jsonify([{"id": f.id, "name": f.name, "product": f.product} for f in farmers])


@farmer_bp.route("/<int:id>", methods=["GET"])
def get_farmer(id):
    """
    Get farmer by ID
    ---
    tags:
      - Farmers
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Farmer found
      404:
        description: Farmer not found
    """
    farmer = Farmer.query.get(id)
    if not farmer:
        return jsonify({"error": "Farmer not found"}), 404
    return jsonify({"id": farmer.id, "name": farmer.name, "product": farmer.product})


@farmer_bp.route("/update/<int:id>", methods=["PUT"])
def update_farmer(id):
    """
    Update farmer
    ---
    tags:
      - Farmers
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
            name:
              type: string
            product:
              type: string
    responses:
      200:
        description: Farmer updated
      404:
        description: Farmer not found
    """
    farmer = Farmer.query.get(id)
    if not farmer:
        return jsonify({"error": "Farmer not found"}), 404
    data = request.json
    farmer.name = data["name"]
    farmer.product = data["product"]
    db.session.commit()
    return jsonify({"message": "Farmer updated"})


@farmer_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_farmer(id):
    """
    Delete farmer
    ---
    tags:
      - Farmers
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Farmer deleted
      404:
        description: Farmer not found
    """
    farmer = Farmer.query.get(id)
    if not farmer:
        return jsonify({"error": "Farmer not found"}), 404
    db.session.delete(farmer)
    db.session.commit()
    return jsonify({"message": "Farmer deleted"})
