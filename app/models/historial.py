from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class HistorialModel(Base):
    __tablename__ = "historial"
    id = Column(Integer, primary_key=True, index=True)
    detalle = Column(String)
    fecha = Column(DateTime, default=datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))