from pydantic import BaseModel
from typing import Optional

class PlantaCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int

class PlantaResponse(PlantaCreate):
    id: int

    class Config:
        from_attributes = True