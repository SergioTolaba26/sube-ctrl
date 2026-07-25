from decimal import Decimal

from domain.entities.linea_movimiento import (
    LineaMovimiento,
)

from domain.enums.tipo_afectacion import (
    TipoAfectacion,
)

from domain.services.movimiento_service import (
    MovimientoService,
)

from domain.services.cuenta_service import (
    CuentaService,
)


class AgregarLineaMovimiento:

    def __init__(
        self,
        movimiento_service: MovimientoService,
        cuenta_service: CuentaService,
    ):
        self.movimiento_service = movimiento_service
        self.cuenta_service = cuenta_service

    def execute(
        self,
        movimiento_id: int,
        cuenta_id: int,
        importe: Decimal,
        tipo_afectacion: TipoAfectacion,
    ):

        movimiento = self.movimiento_service.buscar_por_id(
            movimiento_id,
        )

        if movimiento is None:
            return None

        cuenta = self.cuenta_service.buscar_por_id(
            cuenta_id,
        )

        if cuenta is None:
            raise ValueError(
                "Cuenta inexistente."
            )

        linea = LineaMovimiento(
            cuenta=cuenta,
            importe=importe,
            tipo_afectacion=tipo_afectacion,
        )

        movimiento.agregar_linea(
            linea,
        )

        self.movimiento_service.guardar(
            movimiento,
        )

        return linea