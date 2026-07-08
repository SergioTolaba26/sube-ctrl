from dataclasses import dataclass, field
from decimal import Decimal

from domain.entities.cuenta import Cuenta


@dataclass(slots=True)
class FilaBalanceSumasSaldos:

    cuenta: Cuenta

    total_debitos: Decimal = field(default=Decimal("0"))
    total_creditos: Decimal = field(default=Decimal("0"))

    # @property
    # def saldo(self) -> Decimal:
    #     return Decimal("0")
    
    # @property
    # def saldo(self) -> Decimal:
    #     print(">>> saldo llamado <<<")
    #     return Decimal("0")
    
    @property
    def saldo(self) -> Decimal:
        return self.cuenta.calcular_saldo(
            total_debitos=self.total_debitos,
            total_creditos=self.total_creditos,
        )