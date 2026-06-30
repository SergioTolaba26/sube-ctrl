from fastapi import APIRouter, Depends, HTTPException

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
def list(
    service: TarifaService = Depends(
        get_tarifa_service
    )
):
    return service.list()


@router.get(
    "/{id}",
    response_model=Tarifa
)
def get_by_id(
    id: int,
    service: TarifaService = Depends(
        get_tarifa_service
    )
):

    tarifa = service.get_by_id(id)

    if tarifa is None:

        raise HTTPException(
            status_code=404,
            detail="Tarifa no encontrada."
        )

    return tarifa