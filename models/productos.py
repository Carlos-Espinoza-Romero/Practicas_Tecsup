from db import db
from sqlalchemy import Column, String, Integer, Float, DateTime 


# Definimos las columnas
class ProductosTable(db.Model):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=db.func.now())
