from domain.repositories.ejercicio_repository import (
    EjercicioRepository,
)


class BuscarEjercicio:

    def __init__(
        self,
        repository: EjercicioRepository,
    ):
        self.repository = repository

    def execute(
        self,
        empresa_id: int,
        ejercicio_id: int,
    ):

        return self.repository.buscar_por_id(
            empresa_id,
            ejercicio_id,
        )