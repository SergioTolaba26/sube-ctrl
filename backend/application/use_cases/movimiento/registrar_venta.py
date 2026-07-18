from decimal import Decimal

from domain.entities.movimiento import (
    Movimiento,
)

from domain.entities.linea_movimiento import (
    LineaMovimiento,
)


class RegistrarVenta:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    def execute(
        self,
        fecha,
        descripcion,
        importe,
        cuenta_caja,
        cuenta_ventas,
    ):

        movimiento = Movimiento(
            id=None,
            fecha=fecha,
            descripcion=descripcion,
        )

        movimiento.agregar_linea(
            LineaMovimiento.debito(
                cuenta_caja,
                Decimal(str(importe)),
            )
        )

        movimiento.agregar_linea(
            LineaMovimiento.credito(
                cuenta_ventas,
                Decimal(str(importe)),
            )
        )

        self.repository.guardar(
            movimiento,
        )

        return movimiento