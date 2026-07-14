from domain.services.balance_sumas_saldos import (
    BalanceSumasSaldos,
)


class ConsultarBalanceSumasSaldos:

    def ejecutar(
        self,
        movimientos,
    ):

        servicio = BalanceSumasSaldos()

        return servicio.obtener(
            movimientos=movimientos,
        )