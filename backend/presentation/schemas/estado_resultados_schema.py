from decimal import Decimal

from pydantic import BaseModel

from presentation.schemas.balance_sumas_saldos_schema import (
    BalanceSumasSaldosResponse,
)


class EstadoResultadosResponse(BaseModel):

    ingresos: list[
        BalanceSumasSaldosResponse
    ]

    egresos: list[
        BalanceSumasSaldosResponse
    ]

    total_ingresos: Decimal

    total_egresos: Decimal

    resultado: Decimal