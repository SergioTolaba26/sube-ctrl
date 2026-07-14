from domain.services.estado_resultados import EstadoResultados
from domain.services.generador_movimiento_cierre import (
    GeneradorMovimientoCierre,
)


class ProcesoCierreEjercicio:

    def generar(
        self,
        ejercicio,
        movimientos,
    ):

        #raise NotImplementedError
        estado = EstadoResultados()

        saldos = estado.saldos(
            movimientos,
        )

        generador = GeneradorMovimientoCierre()

        cierre = generador.generar(
            ejercicio=ejercicio,
            saldos=saldos,
        )

        cierre.confirmar()

        ejercicio.cerrar()

        return cierre