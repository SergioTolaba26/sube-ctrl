from fastapi import FastAPI
from presentation.routers.empresa_router import (
    router as empresa_router,
)
app = FastAPI(
    title="Sistema Contable API",
    version="1.0.0",
)
app.include_router(
    empresa_router,
)

@app.get("/")
def root():

    return {
        "mensaje": "Sistema Contable API funcionando",
    }