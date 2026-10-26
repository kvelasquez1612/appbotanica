from fastapi import APIRouter, HTTPException, status
from typing import List

router = APIRouter(prefix="/inventario", tags=["Inventario y Lotes Agrícolas"])

# Simulación temporal de datos para el inventario de la finca
inventario_db = []

@router.get("/", response_model=List[dict])
def listar_inventario():
    """GET /api/v1/inventario: Listar los lotes de cultivos o insumos registrados."""
    return inventario_db

@router.post("/", status_code=status.HTTP_201_CREATED)
def agregar_inventario(item: dict):
    """POST /api/v1/inventario: Agregar un nuevo lote de cultivo o insumo."""
    inventario_db.append(item)
    return {"mensaje": "Registro de inventario agregado con éxito", "item": item}

@router.put("/{id}")
def actualizar_inventario(id: int, item_actualizado: dict):
    """PUT /api/v1/inventario/{id}: Actualizar el estado de un cultivo o insumo."""
    for i, item in enumerate(inventario_db):
        if item.get("id") == id:
            inventario_db[i].update(item_actualizado)
            return {"mensaje": "Inventario actualizado exitosamente", "item": inventario_db[i]}
    raise HTTPException(status_code=404, detail="Ítem de inventario no encontrado")