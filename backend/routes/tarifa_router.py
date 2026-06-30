from fastapi import APIRouter, Depends

from core.dependencies import get_tarifa_service
from models.tarifa import Tarifa
from services.tarifa_service import TarifaService

router = APIRouter(
    prefix="/api/tarifas",
    tags=["Tarifas"]
)


@router.get(
    "",
    response_model=list[Tarifa]
)
def obtener_tarifas(
    service: TarifaService = Depends(get_tarifa_service)
):
    return service.obtener_todas()