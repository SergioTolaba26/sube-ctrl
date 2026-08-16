from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)

from domain.services.balance_general import (
    BalanceGeneral,
)


class ConsultarBalanceGeneral:

    def __init__(
        self,
        repository: MovimientoRepository,
    ):
        self.repository = repository

    def execute(
        self,
    ):
        movimientos = self.repository.listar()

        balance = BalanceGeneral()

        return balance.calcular(
            movimientos,
        )