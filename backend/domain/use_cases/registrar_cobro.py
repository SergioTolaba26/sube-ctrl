from datetime import date

from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento


class RegistrarCobro:

    def ejecutar(
        self,
        caja,
        clientes,
        importe,
        ejercicio,
    ):

        movimiento = Movimiento(
            id=None,
            empresa_id=ejercicio.empresa_id,
            ejercicio_id=ejercicio.id,
            fecha=date.today(),
            descripcion="Cobro",
        )

        movimiento.agregar_linea(
            LineaMovimiento.debito(
                cuenta=caja,
                importe=importe,
            )
        )

        movimiento.agregar_linea(
            LineaMovimiento.credito(
                cuenta=clientes,
                importe=importe,
            )
        )

        movimiento.confirmar()

        return movimiento