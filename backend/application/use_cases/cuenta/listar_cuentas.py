from domain.services.cuenta_service import (
    CuentaService,
)


class ListarCuentas:

    def __init__(
        self,
        service: CuentaService,
    ):
        self.service = service

    def execute(
        self,
    ):

        cuentas = self.service.listar()

        cuentas.sort(
            key=lambda cuenta: (
                cuenta.codigo or ""
            )
        )

        return cuentas