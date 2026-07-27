from application.use_cases.estado_resultados.listar_estado_resultados import (
    ListarEstadoResultados,
)


class CerrarEjercicio:

    def __init__(
        self,
        repository,
        movimiento_service,
        cuenta_service,
    ):
        self.repository = repository
        self.movimiento_service = movimiento_service
        self.cuenta_service = cuenta_service

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

        #
        # Regla 1
        #
        for movimiento in self.movimiento_service.listar():

            if movimiento.esta_en_borrador():

                raise ValueError(
                    "Existen movimientos en borrador."
                )

        #
        # (El asiento de cierre se implementará
        # en el siguiente paso.)
        #

        ejercicio.cerrar()

        self.repository.guardar(
            ejercicio,
        )

        return ejercicio