from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

# Importaciones correctas basadas en tus archivos reales:
from database import get_db  # (Ajusta si tu archivo database.py está en otra ruta, ej: from db.database import get_db)
from models.inventario import InventarioModel
from schemas.inventario import InventarioCreate, InventarioResponse, InventarioUpdate

router = APIRouter(prefix="/inventario", tags=["Inventario"])

@router.get("/", response_model=List[InventarioResponse])
def obtener_inventario(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtiene todos los registros del inventario usando InventarioResponse.
    """
    elementos = db.query(InventarioModel).offset(skip).limit(limit).all()
    return elementos

@router.post("/", response_model=InventarioResponse, status_code=status.HTTP_201_CREATED)
def crear_inventario(item: InventarioCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo registro validando los datos con InventarioCreate y InventarioModel.
    """
    nuevo_elemento = InventarioModel(**item.dict())
    db.add(nuevo_elemento)
    db.commit()
    db.refresh(nuevo_elemento)
    return nuevo_elemento