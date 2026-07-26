from collections import defaultdict

from domain.enums.estado_movimiento import (
    EstadoMovimiento,
)

from domain.enums.tipo_afectacion import (
    TipoAfectacion,
)

from domain.services.movimiento_service import (
    MovimientoService,
)


class ListarLibroMayor:

    def __init__(
        self,
        service: MovimientoService,
    ):
        self.service = service

    def execute(
        self,
    ):

        movimientos = self.service.listar()

        mayor = defaultdict(list)

        for movimiento in movimientos:

            if (
                movimiento.estado
                !=
                EstadoMovimiento.CONFIRMADO
            ):
                continue

            for linea in movimiento.lineas:

                mayor[
                    linea.cuenta.codigo
                ].append(
                    {
                        "fecha": movimiento.fecha,
                        "descripcion": movimiento.descripcion,
                        "cuenta_id": linea.cuenta.id,
                        "codigo": linea.cuenta.codigo,
                        "cuenta": linea.cuenta.nombre,
                        "debito": (
                            linea.importe
                            if linea.tipo_afectacion
                            ==
                            TipoAfectacion.DEBITO
                            else 0
                        ),
                        "credito": (
                            linea.importe
                            if linea.tipo_afectacion
                            ==
                            TipoAfectacion.CREDITO
                            else 0
                        ),
                    }
                )

        resultado = []

        for codigo in sorted(
            mayor.keys(),
        ):

            movimientos = sorted(
                mayor[codigo],
                key=lambda x: x["fecha"],
            )

            resultado.append(
                {
                    "codigo": codigo,
                    "cuenta": movimientos[0]["cuenta"],
                    "cuenta_id": movimientos[0]["cuenta_id"],
                    "movimientos": movimientos,
                }
            )

        return resultado