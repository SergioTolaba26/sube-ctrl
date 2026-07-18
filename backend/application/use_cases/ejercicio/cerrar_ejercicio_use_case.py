from domain.repositories.ejercicio_repository import (
    EjercicioRepository,
)


class CerrarEjercicio:

    def __init__(
        self,
        repository: EjercicioRepository,
    ):
        self.repository = repository

    def execute(
        self,
        ejercicio_id: int,
    ):

        ejercicio = self.repository.buscar_por_id(
            ejercicio_id
        )

        ejercicio.cerrar()

        self.repository.guardar(
            ejercicio
        )

        return ejercicio