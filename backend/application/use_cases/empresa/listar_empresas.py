from domain.repositories.empresa_repository import (
    EmpresaRepository,
)


class ListarEmpresas:

    def __init__(
        self,
        repository: EmpresaRepository,
    ):
        self.repository = repository

    def execute(
        self,
    ):
        return self.repository.obtener_todas()