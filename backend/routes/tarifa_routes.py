from fastapi import APIRouter

from services.tarifa_service import TarifaService

router = APIRouter(
    prefix="/tarifas",
    tags=["Tarifas"]
)

service = TarifaService()


@router.get("")
def obtener_tarifas():
    return service.obtener_todas()