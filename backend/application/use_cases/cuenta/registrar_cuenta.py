from domain.entities.cuenta import Cuenta
from domain.repositories.plan_cuenta_repository import (
    PlanCuentaRepository,
)


class RegistrarCuenta:

    def __init__(
        self,
        repository: PlanCuentaRepository,
    ):
        self.repository = repository

    def execute(
        self,
        codigo: str,
        nombre: str,
        tipo,
    ):

        cuenta = Cuenta(
            id=None,
            codigo=codigo,
            nombre=nombre,
            tipo=tipo,
        )
        self.repository.guardar(cuenta)
        return cuenta
