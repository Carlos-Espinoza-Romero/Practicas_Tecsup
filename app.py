from flask import Flask 
from db import db
from flask_migrate import Migrate 

from models.productos import ProductosTable
from models.ventas import VentasTable


app = Flask(__name__) # Instancia del servidor


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/tattoos_and_swords"

db.init_app(app) # Ya podemos trabajar con sqlalchemy

migrate = Migrate(app, db) # Con estos ya podemos creas las tablas en el servidor

if __name__=='__main__':
    app.run(debug=True) # Ejercución del servidor