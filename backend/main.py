from fastapi import FastAPI
from presentation.routers.empresa_router import (
    router as empresa_router,
)
from presentation.routers.cuenta_router import (
    router as cuenta_router,
)

from presentation.routers.movimiento_router import (
    router as movimiento_router,
)

app = FastAPI(
    title="Sistema Contable API",
    version="1.0.0",
)
app.include_router(
    empresa_router,
)
app.include_router(
    cuenta_router,
)
app.include_router(
    movimiento_router,
)
@app.get("/")
def root():

    return {
        "mensaje": "Sistema Contable API funcionando",
    }