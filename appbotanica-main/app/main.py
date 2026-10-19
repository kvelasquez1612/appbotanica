from fastapi import FastAPI

app = FastAPI(title="FloraCheck API", version="1.0")

@app.get("/")
def inicio():
    return {"mensaje": "¡El servidor ya está funcionando con run.py!"}