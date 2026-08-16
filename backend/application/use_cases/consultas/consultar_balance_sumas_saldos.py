from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)

from domain.services.balance_sumas_saldos import (
    BalanceSumasSaldos,
)


class ConsultarBalanceSumasSaldos:

    def __init__(
        self,
        repository: MovimientoRepository,
    ):
        self.repository = repository

    def execute(
        self,
    ):
        movimientos = self.repository.listar()

        balance = BalanceSumasSaldos()

        return balance.obtener(
            movimientos,
        )