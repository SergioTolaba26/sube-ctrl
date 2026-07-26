from decimal import Decimal

from domain.enums.tipo_afectacion import (
    TipoAfectacion,
)

from domain.services.movimiento_service import (
    MovimientoService,
)

from domain.services.cuenta_service import (
    CuentaService,
)


class ModificarLineaMovimiento:

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
        linea_index: int,
        cuenta_id: int,
        importe: Decimal,
        tipo_afectacion: TipoAfectacion,
    ):

        movimiento = self.movimiento_service.buscar_por_id(
            movimiento_id,
        )

        if movimiento is None:
            return None

        if (
            linea_index < 0
            or
            linea_index >= len(
                movimiento.lineas,
            )
        ):
            raise IndexError(
                "Línea inexistente."
            )

        cuenta = self.cuenta_service.buscar_por_id(
            cuenta_id,
        )

        if cuenta is None:
            raise ValueError(
                "Cuenta inexistente."
            )

        movimiento.modificar_linea(
            linea_index=linea_index,
            cuenta=cuenta,
            importe=importe,
            tipo_afectacion=tipo_afectacion,
        )

        self.movimiento_service.guardar(
            movimiento,
        )

        return movimiento.lineas[
            linea_index
        ]