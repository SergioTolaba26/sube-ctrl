from datetime import date

from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento


class RegistrarPago:

    def ejecutar(
        self,
        caja,
        proveedores,
        importe,
        ejercicio,
    ):

        movimiento = Movimiento(
            id=None,
            empresa_id=ejercicio.empresa_id,
            ejercicio_id=ejercicio.id,
            fecha=date.today(),
            descripcion="Pago",
        )

        movimiento.agregar_linea(
            LineaMovimiento.debito(
                cuenta=proveedores,
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