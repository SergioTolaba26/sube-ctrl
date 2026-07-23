from fastapi import APIRouter
from services.sube_service import (
    obtener_saldo,
    obtener_tarifas,
    obtener_movimientos
)

router = APIRouter(prefix="/sube", tags=["SUBE"])


@router.get("/saldo")
def saldo():
    return {
        "saldo": obtener_saldo()
    }


@router.get("/tarifas")
def tarifas():
    return obtener_tarifas()


@router.get("/movimientos")
def movimientos():
    return obtener_movimientos()