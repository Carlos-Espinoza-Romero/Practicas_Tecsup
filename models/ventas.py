from db import db
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey

class VentasTable(db.Model):
    __tablename__="ventas"

    id = Column(Integer, primary_key=True)
    cantidad = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)
    producto_id = Column(DateTime, ForeignKey("productos.id"), nullable=False)