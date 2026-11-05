from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base

class DiagnosticoModel(Base):
    __tablename__ = "diagnostico"
    id = Column(Integer, primary_key=True, index=True)
    enfermedad = Column(String, index=True)
    tratamiento = Column(Text)
    planta_id = Column(Integer, ForeignKey("plantas.id"), nullable=True)