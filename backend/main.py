from fastapi import FastAPI

from routes.tarifa_router import router as tarifa_router

app = FastAPI(
    title="Transporte Control API",
    version="1.0.0"
)

app.include_router(tarifa_router)


@app.get("/")
def root():
    return {
        "mensaje": "Transporte Control API funcionando"
    }