from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/status")
def status_api():
    return {"estado": "API funcionando correctamente"}