from domain.repositories.empresa_repository import (
    EmpresaRepository,
)


class EliminarEmpresa:

    def __init__(
        self,
        repository: EmpresaRepository,
    ):
        self.repository = repository

    def execute(
        self,
        empresa_id: int,
    ):

        empresa = self.repository.buscar_por_id(
            empresa_id,
        )

        if empresa is None:
            return False

        self.repository.eliminar(
            empresa_id,
        )

        return True