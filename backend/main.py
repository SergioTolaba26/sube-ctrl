from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os
import psycopg
from dotenv import load_dotenv
load_dotenv()

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


load_dotenv()


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


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://localhost:5173",
        "https://cloud-conta-frontend.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# SUPABASE / POSTGRESQL
# ============================================================

@app.get("/test-db")
def test_db():

    database_url = os.getenv(
        "DATABASE_URL",
    )

    if not database_url:

        return {
            "ok": False,
            "error": "DATABASE_URL no está definida",
        }

    try:

        with psycopg.connect(
            database_url,
        ) as conn:

            with conn.cursor() as cursor:

                cursor.execute(
                    "SELECT 1",
                )

                result = cursor.fetchone()

        return {
            "ok": True,
            "database": "Supabase PostgreSQL",
            "result": result[0],
        }

    except Exception as e:

        return {
            "ok": False,
            "error": str(e),
        }
    
# Test PostgreSQL para Producto
@app.get("/test-productos-db")
def test_productos_db():

    database_url = os.getenv(
        "DATABASE_URL",
    )

    if not database_url:
        return {
            "ok": False,
            "error": "DATABASE_URL no está definida",
        }

    try:

        with psycopg.connect(
            database_url,
        ) as conn:

            with conn.cursor() as cursor:

                cursor.execute(
                    """
                    SELECT
                        current_database(),
                        current_schema(),
                        COUNT(*)
                    FROM productos
                    """
                )

                fila = cursor.fetchone()

        return {
            "ok": True,
            "database": fila[0],
            "schema": fila[1],
            "productos": fila[2],
        }

    except Exception as e:

        return {
            "ok": False,
            "error": str(e),
        }