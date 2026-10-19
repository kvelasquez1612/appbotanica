from fastapi import APIRouter
from app.api.plantas import router as plantas_router

api_router = APIRouter()

# Incluir las rutas de plantas con el prefijo /v1
api_router.include_router(plantas_router)