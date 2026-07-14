from domain.services.estado_resultados import (
    EstadoResultados,
)


class ConsultarEstadoResultados:

    def ejecutar(
        self,
        movimientos,
    ):

        servicio = EstadoResultados()

        return servicio.calcular(
            movimientos=movimientos,
        )