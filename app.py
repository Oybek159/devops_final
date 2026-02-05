from flask import Flask
from flasgger import Swagger
# from database.db import db     # DB kerak emas
from routes.farmer_routes import farmer_bp
from routes.supplier_routes import supplier_bp
from routes.procurement_routes import procurement_bp
import os

app = Flask(__name__)
swagger = Swagger(app)

# DB config — o'chirilgan
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)

# Blueprints
app.register_blueprint(farmer_bp, url_prefix="/farmers")
app.register_blueprint(supplier_bp, url_prefix="/suppliers")
app.register_blueprint(procurement_bp, url_prefix="/procurement")

if __name__ == "__main__":
    # Database create_all() — o'chiriladi
    # with app.app_context():
    #     db.create_all()

    app.run(host="0.0.0.0", debug=True)
