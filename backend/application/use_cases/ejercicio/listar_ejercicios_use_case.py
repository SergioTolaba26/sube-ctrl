from domain.repositories.ejercicio_repository import (
    EjercicioRepository,
)


class ListarEjercicios:

    def __init__(
        self,
        repository: EjercicioRepository,
    ):
        self.repository = repository

    def execute(
        self,
    ):
        return self.repository.obtener_todas()