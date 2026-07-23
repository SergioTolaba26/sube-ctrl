from domain.entities.cuenta import Cuenta

from domain.services.cuenta_service import (
    CuentaService,
)


class RegistrarCuenta:

    def __init__(
        self,
        service: CuentaService,
    ):
        self.service = service

    def execute(
        self,
        codigo: str,
        nombre: str,
        tipo,
        imputable: bool = True,
    ):

        cuenta = Cuenta(
            id=None,
            codigo=codigo,
            nombre=nombre,
            tipo=tipo,
            imputable=imputable,
        )

        self.service.guardar(
            cuenta,
        )

        return cuenta