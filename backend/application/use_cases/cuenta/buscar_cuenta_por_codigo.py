from domain.services.cuenta_service import (
    CuentaService,
)


class BuscarCuentaPorCodigo:

    def __init__(
        self,
        service: CuentaService,
    ):
        self.service = service

    def execute(
        self,
        codigo: str,
    ):

        return self.service.buscar_por_codigo(
            codigo,
        )