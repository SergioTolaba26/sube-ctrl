from datetime import date

from domain.entities.movimiento import Movimiento
from domain.entities.linea_movimiento import LineaMovimiento


class RegistrarVenta:

    def ejecutar(
        self,
        caja,
        ventas,
        importe,
        ejercicio,
    ):

        movimiento = Movimiento(
            id=None,
            empresa_id=ejercicio.empresa_id,
            ejercicio_id=ejercicio.id,
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