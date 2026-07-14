from dataclasses import dataclass
from decimal import Decimal

from domain.services.fila_balance_sumas_saldos import (
    FilaBalanceSumasSaldos,
)


@dataclass(slots=True)
class BalanceGeneralCalculado:

    activos: list[FilaBalanceSumasSaldos]

    pasivos: list[FilaBalanceSumasSaldos]

    patrimonio: list[FilaBalanceSumasSaldos]

    total_activos: Decimal

    total_pasivos: Decimal

    total_patrimonio: Decimal