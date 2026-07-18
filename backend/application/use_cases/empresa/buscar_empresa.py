from domain.repositories.empresa_repository import (
    EmpresaRepository,
)


class BuscarEmpresa:

    def __init__(
        self,
        repository: EmpresaRepository,
    ):
        self.repository = repository

    def execute(
        self,
        empresa_id: int,
    ):
        return self.repository.buscar_por_id(
            empresa_id
        )