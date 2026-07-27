from application.use_cases.estado_resultados.listar_estado_resultados import (
    ListarEstadoResultados,
)


class CerrarEjercicio:

    def __init__(
        self,
        repository,
        movimiento_service,
    ):
        self.repository = repository
        self.movimiento_service = movimiento_service

    def execute(
        self,
        ejercicio_id: int,
    ):

        ejercicio = self.repository.buscar_por_id(
            ejercicio_id,
        )

        if ejercicio is None:
            raise ValueError(
                "Ejercicio inexistente."
            )

        movimientos = self.movimiento_service.listar()

        for movimiento in movimientos:

            if (
                hasattr(
                    movimiento,
                    "confirmado",
                )
                and
                not movimiento.confirmado
            ):
                raise ValueError(
                    "Existen movimientos borrador."
                )

        self._generar_asiento_cierre(
            ejercicio,
        )

        ejercicio.cerrar()

        self.repository.guardar(
            ejercicio,
        )

        return ejercicio

    def _validar_movimientos_pendientes(
        self,
        ejercicio,
    ):

        movimientos = (
            self.movimiento_service.listar()
        )

        for movimiento in movimientos:

            if (
                movimiento.ejercicio_id
                ==
                ejercicio.id
                and
                not movimiento.confirmado
            ):
                raise ValueError(
                    "No puede cerrarse un ejercicio con movimientos sin confirmar."
                )

    def _generar_asiento_cierre(
        self,
        ejercicio,
    ):
        """
        Placeholder.

        En el próximo paso se generará el asiento
        de cierre utilizando el Estado de Resultados.
        """

        return None