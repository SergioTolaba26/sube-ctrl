
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
        empresa_id: int,
        codigo: str,
    ):

        return self.service.buscar_por_codigo(
            empresa_id,
            codigo,
        )

