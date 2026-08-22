from fastapi import (
    APIRouter,
    Depends,
)

from presentation.dependencies import (
    get_application_factory,
)

from presentation.schemas.balance_general_schema import (
    BalanceGeneralResponse,
)

router = APIRouter(
    prefix="/balance-general",
    tags=["Balance General"],
)


@router.get(
    "/",
    response_model=BalanceGeneralResponse,
)
def listar_balance_general(
    factory=Depends(
        get_application_factory,
    ),
):

    use_case = factory.listar_balance_general()

    return use_case.execute()