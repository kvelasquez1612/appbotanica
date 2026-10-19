# app/api/diagnostico.py

from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.ia_service import analizar_imagen_planta

router = APIRouter(prefix="/diagnostico", tags=["Diagnóstico IA"])

@router.post("/analizar")
async def analizar_planta(file: UploadFile = File(...)):
    """
    Endpoint que recibe la foto de la planta tomada por el usuario en la app móvil,
    ejecuta el modelo de IA y devuelve el diagnóstico y plan de tratamiento.
    """
    # Validar que el archivo sea una imagen
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="El archivo enviado no es una imagen válida.")
    
    try:
        # Leer los bytes de la imagen recibida
        imagen_bytes = await file.read()
        
        # Procesar con el servicio de IA
        resultado = await analizar_imagen_planta(imagen_bytes)
        
        return {
            "estado": "exitoso",
            "mensaje": "Diagnóstico generado correctamente",
            "data": resultado
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")