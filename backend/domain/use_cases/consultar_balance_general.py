from domain.services.balance_general import (
    BalanceGeneral,
)


class ConsultarBalanceGeneral:

    def ejecutar(
        self,
        movimientos,
    ):

        return BalanceGeneral().calcular(
            movimientos=movimientos,
        )