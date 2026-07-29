from application.services.cierre_contable_service import (
    CierreContableService,
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
        # Generar asiento de cierre
        #
        servicio_cierre = CierreContableService(
            self.movimiento_service,
            self.cuenta_service,
        )

        movimiento = servicio_cierre.generar_asiento_cierre(
            ejercicio,
        )

        #
        # Si el movimiento tiene líneas,
        # se confirma y se guarda.
        #
        if movimiento.tiene_lineas():
            print("===== LINEAS DEL CIERRE =====")

            for linea in movimiento.lineas:

                print(
                    linea.cuenta.codigo,
                    linea.tipo_afectacion,
                    linea.importe,
                )

            print("=============================")
            movimiento.confirmar()

            self.movimiento_service.guardar(
                movimiento,
            )

        #
        # Cerrar ejercicio
        #
        ejercicio.cerrar()

        self.repository.guardar(
            ejercicio,
        )

        return ejercicio