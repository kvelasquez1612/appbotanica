from fastapi import APIRouter
from app.api.plantas import router as plantas_router
from app.api.usuarios import router as usuarios_router
from app.api.inventario import router as inventario_router
from app.api.historial import router as historial_router

api_router = APIRouter()

@api_router.get("/status")
def status_api():
    return {"estado": "API funcionando correctamente"}

# Incluir las rutas de los diferentes módulos del equipo
api_router.include_router(plantas_router)
api_router.include_router(usuarios_router)
api_router.include_router(inventario_router)
api_router.include_router(historial_router)
