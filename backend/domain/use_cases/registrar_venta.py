from datetime import date

from domain.entities.movimiento import Movimiento
from domain.entities.linea_movimiento import LineaMovimiento


class RegistrarVenta:

    def ejecutar(
        self,
        caja,
        ventas,
        importe,
    ):

        movimiento = Movimiento(
            id=None,
            fecha=date.today(),
            descripcion="Venta",
        )

        movimiento.agregar_linea(
            LineaMovimiento.debito(
                cuenta=caja,
                importe=importe,
            )
        )

        movimiento.agregar_linea(
            LineaMovimiento.credito(
                cuenta=ventas,
                importe=importe,
            )
        )

        movimiento.confirmar()

        return movimiento