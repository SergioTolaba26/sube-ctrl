from domain.services.cuenta_service import (
    CuentaService,
)


class EliminarCuenta:

    def __init__(
        self,
        service: CuentaService,
    ):
        self.service = service

    def execute(
        self,
        cuenta_id: int,
        empresa_id: int = 1,
    ):

        cuenta = self.service.buscar_por_id(
            empresa_id,
            cuenta_id,
        )

        if cuenta is None:

            return None

        self.service.eliminar(
            empresa_id,
            cuenta_id,
        )

        return cuenta