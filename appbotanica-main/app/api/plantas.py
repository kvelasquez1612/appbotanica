from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter(prefix="/plantas", tags=["Plantas"])

# --- 1. SCHEMAS DE PYDANTIC PARA VALIDACIÓN ---
class PlantaCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int

class PlantaResponse(PlantaCreate):
    id: int

    class Config:
        from_attributes = True

# Simulación temporal de datos (luego lo conectarás con SQLAlchemy)
plantas_db = []
id_counter = 1  # Contador para asignar IDs automáticos

# --- 2. ENDPOINT GET: Listar plantas (con filtro opcional) ---
@router.get("/", response_model=List[PlantaResponse])
def listar_plantas(busqueda: str = None):
    """GET /api/v1/plantas: Listar todas las especies de plantas"""
    if busqueda:
        filtradas = [p for p in plantas_db if busqueda.lower() in p["nombre"].lower()]
        return filtradas
    return plantas_db

# --- 3. ENDPOINT GET POR ID: Obtener planta específica ---
@router.get("/{id}", response_model=PlantaResponse)
def obtener_planta(id: int):
    """GET /api/v1/plantas/{id}: Obtener la ficha técnica de una planta específica"""
    for planta in plantas_db:
        if planta["id"] == id:
            return planta
    raise HTTPException(status_code=404, detail="Planta no encontrada")

# --- 4. ENDPOINT POST: Registrar nueva planta ---
@router.post("/", response_model=PlantaResponse, status_code=status.HTTP_201_CREATED)
def crear_planta(planta: PlantaCreate):
    """POST /api/v1/plantas: Registrar una nueva especie vegetal"""
    global id_counter
    
    # Convertir el modelo de Pydantic a diccionario y agregarle el ID
    nueva_planta = planta.model_dump()
    nueva_planta["id"] = id_counter
    
    # Guardar en la base de datos simulada
    plantas_db.append(nueva_planta)
    id_counter += 1
    
    return nueva_planta