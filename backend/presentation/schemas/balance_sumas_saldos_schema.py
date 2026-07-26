from decimal import Decimal

from pydantic import BaseModel


class BalanceSumasSaldosResponse(BaseModel):

    cuenta_id: int

    codigo: str

    cuenta: str

    debitos: Decimal

    creditos: Decimal

    saldo: Decimal