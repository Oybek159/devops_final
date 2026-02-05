from flask import Blueprint, request, jsonify
from database.models import Procurement
from database.db import db

procurement_bp = Blueprint("procurement", __name__)

@procurement_bp.route("/order", methods=["POST"])
def create_order():
    """
    Create procurement order
    ---
    tags:
      - Procurement
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - farmer_id
            - supplier_id
          properties:
            farmer_id:
              type: integer
            supplier_id:
              type: integer
    responses:
      201:
        description: Order created
    """
    data = request.json
    order = Procurement(
        farmer_id=data["farmer_id"],
        supplier_id=data["supplier_id"],
        status="Pending"
    )
    db.session.add(order)
    db.session.commit()
    return jsonify({"message": "Order created"}), 201


@procurement_bp.route("/", methods=["GET"])
def get_orders():
    """
    Get all orders
    ---
    tags:
      - Procurement
    responses:
      200:
        description: List of all orders
    """
    orders = Procurement.query.all()
    return jsonify([
        {"id": o.id, "farmer_id": o.farmer_id,
         "supplier_id": o.supplier_id, "status": o.status}
        for o in orders
    ])


@procurement_bp.route("/update/<int:id>", methods=["PUT"])
def update_status(id):
    """
    Update order status
    ---
    tags:
      - Procurement
    parameters:
      - in: path
        name: id
        required: true
        type: integer
      - in: body
        name: body
        schema:
          properties:
            status:
              type: string
    responses:
      200:
        description: Status updated
      404:
        description: Order not found
    """
    order = Procurement.query.get(id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    order.status = request.json["status"]
    db.session.commit()
    return jsonify({"message": "Status updated"})


@procurement_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_order(id):
    """
    Delete order
    ---
    tags:
      - Procurement
    parameters:
      - in: path
        name: id
        required: true
        type: integer
    responses:
      200:
        description: Order deleted
      404:
        description: Order not found
    """
    order = Procurement.query.get(id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted"})
