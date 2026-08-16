from fastapi import FastAPI
from presentation.routers.empresa_router import (
    router as empresa_router,
)
from presentation.routers.cuenta_router import (
    router as cuenta_router,
)

from presentation.routers.libro_diario_router import (
    router as libro_diario_router,
)

from presentation.routers.libro_mayor_router import (
    router as libro_mayor_router,
)
from presentation.routers.balance_sumas_saldos_router import (
    router as balance_sumas_saldos_router,
)
from presentation.routers.balance_general_router import (
    router as balance_general_router,
)
from presentation.routers.estado_resultados_router import (
    router as estado_resultados_router,
)
from presentation.routers.ejercicio_router import (
    router as ejercicio_router,
)

from presentation.routers.asiento_router import (
    router as asiento_router,
)
from presentation.routers.producto_router import (
    router as producto_router,
)
from fastapi.middleware.cors import CORSMiddleware

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
    libro_diario_router,
)
app.include_router(
    libro_mayor_router,
)
app.include_router(
    balance_sumas_saldos_router,
)
app.include_router(
    balance_general_router,
)
app.include_router(
    ejercicio_router,
)

app.include_router(
    estado_resultados_router,
)
app.include_router(
    asiento_router,
)
app.include_router(
    producto_router,
)
@app.get("/")
def root():

    return {
        "mensaje": "Sistema Contable API funcionando",
    }

# frontend
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5173",
        "http://localhost:5173",
        "http://127.0.0.1:5500",

        "http://192.168.0.9:5500",  # IP de tu laptop en casa
        "http://192.168.3.124:5173", # IP del trabajo
        "http://192.168.0.9:5173",
        "http://192.168.0.13:5173",
    ],
   # allow_origins=["*"], # Mejor aún sirve para cualquier IP, uso sólo en desarrollo


    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)