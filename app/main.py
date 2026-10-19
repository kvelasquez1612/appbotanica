from fastapi import FastAPI

app = FastAPI(
  title="API floracheck",
  description="backend con clean architecture",
  version="1.0.0"
)

@app.get("/")
def leer_raiz():
  return{"mensaje":"backend inicializado correctamente"}