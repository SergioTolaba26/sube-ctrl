from decimal import Decimal

from domain.entities.linea_movimiento import (
    LineaMovimiento,
)
from domain.entities.movimiento import (
    Movimiento,
)
from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)


class RegistrarCobro:

    def __init__(
        self,
        repository: MovimientoRepository,
    ):
        self.repository = repository

    def execute(
        self,
        fecha,
        descripcion,
        importe,
        cuenta_caja,
        cuenta_clientes,
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
                cuenta_clientes,
                Decimal(str(importe)),
            )
        )

        self.repository.guardar(
            movimiento,
        )

        return movimiento