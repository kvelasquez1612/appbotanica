from fastapi import FastAPI
from app.api.v1_router import api_router

app = FastAPI(
    title="App Botánica API",
    version="1.0.0",
    description="API para la gestión de plantas, productos e inventario"
)

# Conectar el router bajo la versión /api/v1
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"mensaje": "API de App Botánica funcionando correctamente 🌿"}