from fastapi import FastAPI
from app.core.config import settings
from app.api.v1_router import api_router

# Inicializamos FastAPI usando las variables del archivo de configuración (.env)
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Backend con Clean Architecture para FloraCheck"
)

# Incluimos las rutas principales usando el prefijo configurado
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def leer_raiz():
    return {
        "mensaje": "¡Backend inicializado correctamente!",
        "proyecto": settings.PROJECT_NAME,
        "version": settings.VERSION
    }