from decimal import Decimal

from domain.entities.linea_movimiento import (
    LineaMovimiento,
)

from domain.enums.tipo_afectacion import (
    TipoAfectacion,
)


class LineaMovimientoMapper:

    @staticmethod
    def to_dict(
        linea,
    ):
        return {
            "cuenta_id": linea.cuenta.id,
            "importe": str(
                linea.importe,
            ),
            "tipo_afectacion":
                linea.tipo_afectacion.name,
        }

    @staticmethod
    def from_dict(
        datos,
        cuenta_repository,
    ):

        cuenta = cuenta_repository.buscar_por_id(
            datos["cuenta_id"],
        )

        return LineaMovimiento(
            cuenta=cuenta,
            importe=Decimal(
                datos["importe"],
            ),
            tipo_afectacion=TipoAfectacion[
                datos["tipo_afectacion"]
            ],
        )

    @staticmethod
    def to_dict_list(
        lineas,
    ):
        return [
            LineaMovimientoMapper.to_dict(
                linea,
            )
            for linea in lineas
        ]
    
    @staticmethod
    def from_dict_list(
        datos,
        cuenta_repository,
    ):
        return [
            LineaMovimientoMapper.from_dict(
                dato,
                cuenta_repository,
            )
            for dato in datos
        ]
    