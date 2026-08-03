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


class ModificarMovimiento:

    def __init__(
        self,
        service: MovimientoService,
        cuenta_service: CuentaService,
    ):
        self.service = service
        self.cuenta_service = cuenta_service

    def execute(
        self,
        movimiento_id: int,
        fecha,
        descripcion: str,
        estado,
        lineas,
    ):

        movimiento = self.service.buscar_por_id(
            movimiento_id,
        )

        if movimiento is None:
            return None

        if not movimiento.esta_en_borrador():
            raise ValueError(
                "No se puede modificar un movimiento confirmado."
            )

        #
        # Cabecera
        #
        movimiento.fecha = fecha

        movimiento.cambiar_descripcion(
            descripcion,
        )

        if estado is not None:
            movimiento.estado = estado

        #
        # Reemplazar completamente las líneas
        #
        if lineas is not None:

            movimiento.lineas.clear()

            for linea in lineas:

                cuenta = self.cuenta_service.buscar_por_id(
                    linea.cuenta_id,
                )

                if cuenta is None:
                    raise ValueError(
                        f"Cuenta inexistente: {linea.cuenta_id}"
                    )

                if (
                    linea.tipo_afectacion
                    == TipoAfectacion.DEBITO
                ):

                    nueva_linea = LineaMovimiento.debito(
                        cuenta,
                        Decimal(
                            str(linea.importe),
                        ),
                    )

                else:

                    nueva_linea = LineaMovimiento.credito(
                        cuenta,
                        Decimal(
                            str(linea.importe),
                        ),
                    )

                movimiento.agregar_linea(
                    nueva_linea,
                )

        self.service.guardar(
            movimiento,
        )

        return movimiento