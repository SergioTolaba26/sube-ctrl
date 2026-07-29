from domain.services.ejercicio_service import (
    EjercicioService,
)


class ListarEjercicios:

    def __init__(
        self,
        service: EjercicioService,
    ):
        self.service = service

    def execute(
        self,
    ):
        return self.service.listar()