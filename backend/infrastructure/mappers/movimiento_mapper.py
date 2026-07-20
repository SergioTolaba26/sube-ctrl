from datetime import date

from domain.entities.movimiento import (
    Movimiento,
)

from domain.enums.estado_movimiento import (
    EstadoMovimiento,
)
from infrastructure.mappers.linea_movimiento_mapper import LineaMovimientoMapper
class MovimientoMapper:

    @staticmethod
    def to_dict(
        movimiento,
    ):
        return {
            "id": movimiento.id,
            "fecha": movimiento.fecha.isoformat(),
            "descripcion": movimiento.descripcion,
            "estado": movimiento.estado.name,
            "lineas": LineaMovimientoMapper.to_dict_list(
                movimiento.lineas,
            ),
        }
    
    @staticmethod
    def from_dict(
        datos,
        cuenta_repository,
    ):

        return Movimiento(
            id=datos["id"],

            fecha=date.fromisoformat(
                datos["fecha"],
            ),

            descripcion=datos["descripcion"],

            estado=EstadoMovimiento[
                datos["estado"]
            ],

            lineas=LineaMovimientoMapper.from_dict_list(
                datos["lineas"],
                cuenta_repository,
            ),
        )
    
    @staticmethod
    def to_dict_list(
        movimientos,
    ):
        return [
            MovimientoMapper.to_dict(
                movimiento,
            )
            for movimiento in movimientos
        ]
    
    @staticmethod
    def from_dict_list(
        datos,
        cuenta_repository,
    ):
        return [
            MovimientoMapper.from_dict(
                dato,
                cuenta_repository,
            )
            for dato in datos
        ]