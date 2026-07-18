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
        ejercicio_id: int,
    ):
        return self.repository.buscar_por_id(
            ejercicio_id
        )