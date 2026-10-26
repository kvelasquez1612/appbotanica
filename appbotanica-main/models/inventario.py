from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class InventarioModel(Base):
    __tablename__ = "inventario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    tipo = Column(String, nullable=False)
    area_m2 = Column(Float, nullable=True)
    estado_cultivo = Column(String, nullable=True)
    cantidad = Column(Float, nullable=True)
    unidad_medida = Column(String, nullable=True)
    descripcion = Column(String, nullable=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)