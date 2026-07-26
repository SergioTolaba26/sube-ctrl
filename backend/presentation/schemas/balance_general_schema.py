from decimal import Decimal

from pydantic import BaseModel


class BalanceGeneralCuentaResponse(BaseModel):

    cuenta_id: int

    codigo: str

    cuenta: str

    debitos: Decimal

    creditos: Decimal

    saldo: Decimal


class BalanceGeneralResponse(BaseModel):

    activos: list[
        BalanceGeneralCuentaResponse
    ]

    pasivos: list[
        BalanceGeneralCuentaResponse
    ]

    patrimonio: list[
        BalanceGeneralCuentaResponse
    ]

    total_activo: Decimal

    total_pasivo: Decimal

    total_patrimonio: Decimal

    resultado_ejercicio: Decimal

    pasivo_mas_patrimonio: Decimal

    total_pasivo_patrimonio: Decimal

    diferencia: Decimal