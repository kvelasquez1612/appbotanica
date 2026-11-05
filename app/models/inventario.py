from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from app.database import Base

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

Base = declarative_base()

class InventarioModel(Base):
    __tablename__ = "inventario"
    id = Column(Integer, primary_key=True, index=True)
    nombre_producto = Column(String, index=True)
    cantidad = Column(Integer)
    precio_unitario = Column(Float)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))