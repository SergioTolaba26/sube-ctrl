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
        empresa_id: int,
    ):

        cuentas = self.service.listar(
            empresa_id,
        )
        cuentas.sort(
            key=lambda cuenta: (
                cuenta.codigo or ""
            )
        )

        return cuentas