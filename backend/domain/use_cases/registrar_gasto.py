from datetime import date

from domain.entities.movimiento import Movimiento
from domain.entities.linea_movimiento import LineaMovimiento


class RegistrarGasto:

    def ejecutar(
        self,
        caja,
        gastos,
        importe,
        ejercicio,
    ):

        movimiento = Movimiento(
            id=None,
            empresa_id=ejercicio.empresa_id,
            ejercicio_id=ejercicio.id,
            fecha=date.today(),
            descripcion="Gasto",
        )

        movimiento.agregar_linea(
            LineaMovimiento.debito(
                cuenta=gastos,
                importe=importe,
            )
        )

        movimiento.agregar_linea(
            LineaMovimiento.credito(
                cuenta=caja,
                importe=importe,
            )
        )

        movimiento.confirmar()

        return movimiento