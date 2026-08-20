from domain.services.cuenta_service import (
    CuentaService,
)


class BuscarCuenta:

    def __init__(
        self,
        service: CuentaService,
    ):
        self.service = service

    def execute(
        self,
        empresa_id: int,
        cuenta_id: int,
    ):

        return self.service.buscar_por_id(
            empresa_id,
            cuenta_id,
        )