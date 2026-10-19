from fastapi import APIRouter, HTTPException, status
from typing import List

router = APIRouter(prefix="/plantas", tags=["Plantas"])

# Simulación temporal de datos (luego lo conectarás con SQLAlchemy)
plantas_db = []

@router.get("/", response_model=List[dict])
def listar_plantas(busqueda: str = None):
    """GET /api/v1/plantas: Listar todas las especies de plantas"""
    if busqueda:
        filtradas = [p for p in plantas_db if busqueda.lower() in p["nombre"].lower()]
        return filtradas
    return plantas_db

@router.get("/{id}", response_model=dict)
def obtener_planta(id: int):
    """GET /api/v1/plantas/{id}: Obtener la ficha técnica de una planta específica"""
    for planta in plantas_db:
        if planta["id"] == id:
            return planta
    raise HTTPException(status_code=404, detail="Planta no encontrada")

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_planta(planta: dict):
    """POST /api/v1/plantas: Registrar una nueva especie vegetal"""
    plantas_db.append(planta)
    return {"mensaje": "Planta registrada con éxito", "planta": planta}