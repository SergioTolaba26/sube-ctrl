class CierreEjercicio:

    def cerrar(
        self,
        ejercicio,
        movimientos,
    ):

        for movimiento in movimientos:

            if (
                ejercicio.contiene(movimiento.fecha)
                and
                not movimiento.esta_confirmado()
            ):
                raise ValueError(
                    "Existen movimientos pendientes."
                )

        ejercicio.cerrar()