from domain.entities.linea_movimiento import (
    LineaMovimiento,
)
from domain.enums.tipo_afectacion import (
    TipoAfectacion,
)


class ModificarAsiento:

    def __init__(
        self,
        movimiento_service,
        cuenta_service,
    ):
        self.movimiento_service = movimiento_service
        self.cuenta_service = cuenta_service

    def execute(
        self,
        movimiento_id,
        fecha,
        descripcion,
        lineas,
    ):

        movimiento = (
            self.movimiento_service.buscar_por_id(
                movimiento_id,
            )
        )

        if movimiento is None:
            raise ValueError(
                "Asiento no encontrado."
            )

        if movimiento.esta_confirmado():
            raise ValueError(
                "No se puede modificar un asiento confirmado."
            )

        movimiento.fecha = fecha
        movimiento.descripcion = descripcion

        #
        # Reemplazar líneas
        #
        movimiento.lineas = []

        for dato in lineas:

            cuenta = (
                self.cuenta_service.buscar_por_id(
                    dato["cuenta_id"],
                )
            )

            if cuenta is None:
                raise ValueError(
                    f"No existe la cuenta {dato['cuenta_id']}."
                )

            if (
                dato["tipo_afectacion"]
                == TipoAfectacion.DEBITO
            ):

                linea = (
                    LineaMovimiento.debito(
                        cuenta,
                        dato["importe"],
                    )
                )

            else:

                linea = (
                    LineaMovimiento.credito(
                        cuenta,
                        dato["importe"],
                    )
                )

            movimiento.agregar_linea(
                linea,
            )

        self.movimiento_service.guardar(
            movimiento,
        )

        return movimiento