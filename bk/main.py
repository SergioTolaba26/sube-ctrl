from fastapi import FastAPI
from routes.sube_routes import router as sube_router

app = FastAPI(
    title="SUBE Control",
    version="1.0"
)

app.include_router(sube_router)


@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a SUBE Control"
    }