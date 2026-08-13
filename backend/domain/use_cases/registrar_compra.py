from datetime import date

from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento


class RegistrarCompra:

    def ejecutar(
        self,
        caja,
        compras,
        importe,
        ejercicio,
    ):

        movimiento = Movimiento(
            id=None,
            empresa_id=ejercicio.empresa_id,
            ejercicio_id=ejercicio.id,
            fecha=date.today(),
            descripcion="Compra",
        )

        movimiento.agregar_linea(
            LineaMovimiento.debito(
                cuenta=compras,
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