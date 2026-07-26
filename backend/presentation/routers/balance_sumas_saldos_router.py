from fastapi import APIRouter

from application.factory import (
    ApplicationFactory,
)

from presentation.schemas.balance_sumas_saldos_schema import (
    BalanceSumasSaldosResponse,
)

router = APIRouter(
    prefix="/balance-sumas-saldos",
    tags=["Balance de Sumas y Saldos"],
)

factory = ApplicationFactory()


@router.get(
    "/",
    response_model=list[
        BalanceSumasSaldosResponse
    ],
)
def listar_balance_sumas_saldos():

    use_case = factory.listar_balance_sumas_saldos()

    return use_case.execute()