from datetime import date

from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_afectacion import TipoAfectacion


class RegistrarCobro:

    def ejecutar(
        self,
        caja,
        clientes,
        importe,
    ):

        movimiento = Movimiento(
            id=None,
            fecha=date.today(),
            descripcion="Cobro",
        )

        movimiento.agregar_linea(
            LineaMovimiento(
                cuenta=caja,
                importe=importe,
                tipo_afectacion=TipoAfectacion.DEBITO,
            )
        )

        movimiento.agregar_linea(
            LineaMovimiento(
                cuenta=clientes,
                importe=importe,
                tipo_afectacion=TipoAfectacion.CREDITO,
            )
        )
        movimiento.confirmar()
        return movimiento