from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)

from domain.services.estado_resultados import (
    EstadoResultados,
)


class ConsultarEstadoResultados:

    def __init__(
        self,
        repository: MovimientoRepository,
    ):
        self.repository = repository

    def execute(
        self,
    ):
        movimientos = self.repository.listar()

        estado = EstadoResultados()

        return estado.calcular(
            movimientos,
        )