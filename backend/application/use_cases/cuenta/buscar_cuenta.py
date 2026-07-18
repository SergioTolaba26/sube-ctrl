from domain.repositories.plan_cuenta_repository import (
    PlanCuentaRepository,
)


class BuscarCuenta:

    def __init__(
        self,
        repository: PlanCuentaRepository,
    ):
        self.repository = repository

    def execute(
        self,
        codigo: str,
    ):
        return self.repository.buscar_por_codigo(
            codigo
        )