from presentation.schemas.movimiento_resumen_response import (
    MovimientoResumenResponse,
)

from presentation.schemas.movimiento_detalle_response import (
    MovimientoDetalleResponse,
    LineaMovimientoResponse,
)


class MovimientoResponseMapper:

    @staticmethod
    def to_resumen(
        movimiento,
    ) -> MovimientoResumenResponse:

        return MovimientoResumenResponse(
            id=movimiento.id,
            fecha=movimiento.fecha,
            descripcion=movimiento.descripcion,
            estado=movimiento.estado,
        )

    @staticmethod
    def to_detalle(
        movimiento,
    ) -> MovimientoDetalleResponse:

        return MovimientoDetalleResponse(
            id=movimiento.id,
            fecha=movimiento.fecha,
            descripcion=movimiento.descripcion,
            estado=movimiento.estado,
            lineas=[
                LineaMovimientoResponse(
                    cuenta_id=linea.cuenta.id,
                    codigo=linea.cuenta.codigo,
                    cuenta=linea.cuenta.nombre,
                    tipo=linea.tipo_afectacion,
                    importe=linea.importe,
                )
                for linea in movimiento.lineas
            ],
        )