from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1_router import api_router
from app.db.session import engine, Base
from app.models.usuario_model import UsuarioModel

# Crea las tablas automáticamente en Supabase / Base de datos al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Backend con Clean Architecture para AgroFlora"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def leer_raiz():
    return {
        "mensaje": "¡Backend inicializado correctamente!",
        "proyecto": settings.PROJECT_NAME,
        "version": settings.VERSION
    }
