from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class PlantaModel(Base):
    __tablename__ = "plantas"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, nullable=True)
    precio = Column(Float)
    stock = Column(Integer)