from fastapi import (
    APIRouter,
    Depends,
)

from presentation.dependencies import (
    get_application_factory,
)
from presentation.schemas.balance_sumas_saldos_schema import (
    BalanceSumasSaldosResponse,
)

router = APIRouter(
    prefix="/balance-sumas-saldos",
    tags=["Balance de Sumas y Saldos"],
)



@router.get(
    "/",
    response_model=list[
        BalanceSumasSaldosResponse
    ],
)
def listar_balance_sumas_saldos(
    factory=Depends(
        get_application_factory,
    ),
):

    use_case = factory.listar_balance_sumas_saldos()

    return use_case.execute()