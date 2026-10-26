from fastapi import APIRouter, HTTPException, status
from typing import List

router = APIRouter(prefix="/historial", tags=["Historial de Diagnósticos"])

# Simulación temporal de datos para el historial
historial_db = []

@router.get("/", response_model=List[dict])
def consultar_historial():
    """GET /api/v1/historial: Consultar el historial de fotos y diagnósticos."""
    return historial_db

@router.get("/{id}", response_model=dict)
def detalle_historial(id: int):
    """GET /api/v1/historial/{id}: Ver el detalle específico de un diagnóstico pasado."""
    for registro in historial_db:
        if registro.get("id") == id:
            return registro
    raise HTTPException(status_code=404, detail="Registro no encontrado en el historial")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_historial(id: int):
    """DELETE /api/v1/historial/{id}: Eliminar un registro antiguo del historial."""
    for i, registro in enumerate(historial_db):
        if registro.get("id") == id:
            del historial_db[i]
            return
    raise HTTPException(status_code=404, detail="Registro no encontrado en el historial")