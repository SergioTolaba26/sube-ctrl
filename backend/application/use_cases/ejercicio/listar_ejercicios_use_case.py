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
        empresa_id: int | None = None,
    ):

        return self.service.listar(
            empresa_id,
        )