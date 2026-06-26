from fastapi import FastAPI

from routes.tarifa_routes import router as tarifa_router

app = FastAPI(
    title="SUBE Control API",
    version="0.1.0"
)

app.include_router(tarifa_router)


@app.get("/")
def inicio():
    return {
        "mensaje": "API SUBE Control funcionando"
    }