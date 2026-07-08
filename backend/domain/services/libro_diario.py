from domain.services.asiento_libro_diario import AsientoLibroDiario



class LibroDiario:
    """
    Servicio de dominio que construye el Libro Diario.
    """

    def obtener(self, movimientos):

        confirmados = []

        for movimiento in movimientos:
            if movimiento.esta_confirmado():
                confirmados.append(movimiento)

        confirmados.sort(
            key=lambda movimiento: movimiento.fecha
        )

       #return confirmados


        asientos = []

        for movimiento in confirmados:
            asientos.append(
                AsientoLibroDiario(
                    movimiento=movimiento
                )
            )

        return asientos