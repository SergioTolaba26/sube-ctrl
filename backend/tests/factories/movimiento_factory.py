from datetime import date
from decimal import Decimal

from domain.entities.movimiento import (
    Movimiento,
)

from domain.entities.linea_movimiento import (
    LineaMovimiento,
)

from tests.factories.cuenta_factory import (
    CuentaFactory,
)


class MovimientoFactory:

    _id = 1

    @classmethod
    def crear(
        cls,
        descripcion: str = "Movimiento de prueba",
        fecha: date | None = None,
    ) -> Movimiento:

        movimiento = Movimiento(
            id=cls._id,
            fecha=fecha or date.today(),
            descripcion=descripcion,
        )

        cls._id += 1

        return movimiento

    @classmethod
    def venta(
        cls,
        importe: Decimal = Decimal("50000"),
    ) -> Movimiento:

        movimiento = cls.crear(
            descripcion="Venta",
        )

        caja = CuentaFactory.caja()

        ventas = CuentaFactory.ventas()

        movimiento.agregar_linea(
            LineaMovimiento.debito(
                caja,
                importe,
            )
        )

        movimiento.agregar_linea(
            LineaMovimiento.credito(
                ventas,
                importe,
            )
        )

        movimiento.confirmar()

        return movimiento

    @classmethod
    def gasto(
        cls,
        importe: Decimal = Decimal("10000"),
    ) -> Movimiento:

        movimiento = cls.crear(
            descripcion="Gasto",
        )

        alquiler = CuentaFactory.alquiler()

        caja = CuentaFactory.caja()

        movimiento.agregar_linea(
            LineaMovimiento.debito(
                alquiler,
                importe,
            )
        )

        movimiento.agregar_linea(
            LineaMovimiento.credito(
                caja,
                importe,
            )
        )

        movimiento.confirmar()

        return movimiento