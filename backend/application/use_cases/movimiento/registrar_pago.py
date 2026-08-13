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


class RegistrarPago:

    def __init__(
        self,
        repository: MovimientoRepository,
    ):
        self.repository = repository

    def execute(
        self,
        empresa_id: int,
        ejercicio_id: int,
        fecha,
        descripcion,
        importe,
        cuenta_proveedores,
        cuenta_caja,
    ):

        movimiento = Movimiento(
            id=None,
            empresa_id=empresa_id,
            ejercicio_id=ejercicio_id,
            fecha=fecha,
            descripcion=descripcion,
        )

        movimiento.agregar_linea(
            LineaMovimiento.debito(
                cuenta_proveedores,
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