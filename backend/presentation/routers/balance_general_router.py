from fastapi import APIRouter

from application.factory import (
    ApplicationFactory,
)

from presentation.schemas.balance_general_schema import (
    BalanceGeneralResponse,
)

router = APIRouter(
    prefix="/balance-general",
    tags=["Balance General"],
)

factory = ApplicationFactory()


@router.get(
    "/",
    response_model=BalanceGeneralResponse,
)
def listar_balance_general():

    use_case = factory.listar_balance_general()

    return use_case.execute()