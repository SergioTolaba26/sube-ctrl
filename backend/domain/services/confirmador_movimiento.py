class ConfirmadorMovimiento:

    def confirmar(
        self,
        movimiento,
        ejercicio,
    ):

        if ejercicio.esta_cerrado():
            raise ValueError(
                "El ejercicio está cerrado."
            )

        movimiento.confirmar()

    