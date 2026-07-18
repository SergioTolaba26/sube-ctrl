from decimal import Decimal

from domain.entities.movimiento import Movimiento
from domain.entities.linea_movimiento import LineaMovimiento


class RegistrarCompra:

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
        cuenta_compras,
        cuenta_caja,
    ):

        movimiento = Movimiento(
            id=None,
            fecha=fecha,
            descripcion=descripcion,
        )

        movimiento.agregar_linea(
            LineaMovimiento.debito(
                cuenta_compras,
                Decimal(str(importe)),
            )
        )

        movimiento.agregar_linea(
            LineaMovimiento.credito(
                cuenta_caja,
                Decimal(str(importe)),
            )
        )

        self.repository.guardar(
            movimiento,
        )

        return movimiento