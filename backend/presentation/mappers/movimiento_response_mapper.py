from presentation.schemas.linea_movimiento_schema import (
    LineaMovimientoResponse,
)

from presentation.schemas.movimiento_detalle_response import (
    MovimientoDetalleResponse,
)

from presentation.schemas.movimiento_resumen_response import (
    MovimientoResumenResponse,
)



class MovimientoResponseMapper:

    @staticmethod
    def to_resumen(
        movimiento,
    ) -> MovimientoResumenResponse:

        return MovimientoResumenResponse(
            id=movimiento.id,
            numero_asiento=movimiento.numero_asiento,
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
            numero_asiento=movimiento.numero_asiento,
            fecha=movimiento.fecha,
            descripcion=movimiento.descripcion,
            estado=movimiento.estado,
            lineas=[
                LineaMovimientoResponse(
                    cuenta_id=linea.cuenta.id,
                    cuenta_codigo=linea.cuenta.codigo,
                    cuenta_nombre=linea.cuenta.nombre,
                    importe=linea.importe,
                    tipo_afectacion=linea.tipo_afectacion,
                )
                for linea in movimiento.lineas
            ],
        )