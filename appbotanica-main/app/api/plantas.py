from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.planta_schemas import PlantaCreate, PlantaResponse

router = APIRouter(prefix="/plantas", tags=["Plantas"])

# Simulación temporal de datos
plantas_db = []
id_counter = 1

@router.get("/", response_model=List[PlantaResponse])
def listar_plantas(busqueda: str = None):
    """GET /api/v1/plantas: Listar todas las especies de plantas"""
    if busqueda:
        filtradas = [p for p in plantas_db if busqueda.lower() in p["nombre"].lower()]
        return filtradas
    return plantas_db

@router.get("/{id}", response_model=PlantaResponse)
def obtener_planta(id: int):
    """GET /api/v1/plantas/{id}: Obtener la ficha técnica de una planta específica"""
    for planta in plantas_db:
        if planta["id"] == id:
            return planta
    raise HTTPException(status_code=404, detail="Planta no encontrada")

@router.post("/", response_model=PlantaResponse, status_code=status.HTTP_201_CREATED)
def crear_planta(planta: PlantaCreate):
    """POST /api/v1/plantas: Registrar una nueva especie vegetal"""
    global id_counter
    
    nueva_planta = planta.model_dump()
    nueva_planta["id"] = id_counter
    
    plantas_db.append(nueva_planta)
    id_counter += 1
    
    return nueva_planta
