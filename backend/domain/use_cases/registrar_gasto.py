from datetime import date

from domain.entities.movimiento import Movimiento
from domain.entities.linea_movimiento import LineaMovimiento
from domain.enums.tipo_afectacion import TipoAfectacion


class RegistrarGasto:

    def ejecutar(
        self,
        caja,
        gastos,
        importe,
    ):

        movimiento = Movimiento(
            id=None,
            fecha=date.today(),
            descripcion="Gasto",
        )

        movimiento.agregar_linea(
            LineaMovimiento(
                cuenta=gastos,
                importe=importe,
                tipo_afectacion=TipoAfectacion.DEBITO,
            )
        )

        movimiento.agregar_linea(
            LineaMovimiento(
                cuenta=caja,
                importe=importe,
                tipo_afectacion=TipoAfectacion.CREDITO,
            )
        )
        movimiento.confirmar()
        return movimiento