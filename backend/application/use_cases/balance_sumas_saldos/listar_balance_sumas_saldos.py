from collections import defaultdict
from decimal import Decimal

from domain.enums.estado_movimiento import (
    EstadoMovimiento,
)

from domain.enums.tipo_afectacion import (
    TipoAfectacion,
)

from domain.services.movimiento_service import (
    MovimientoService,
)


class ListarBalanceSumasSaldos:

    def __init__(
        self,
        service: MovimientoService,
    ):
        self.service = service

    def execute(
        self,
    ):

        movimientos = self.service.listar()

        cuentas = defaultdict(
            lambda: {
                "cuenta_id": None,
                "codigo": "",
                "cuenta": "",
                "debitos": Decimal("0"),
                "creditos": Decimal("0"),
            }
        )

        for movimiento in movimientos:

            if (
                movimiento.estado
                !=
                EstadoMovimiento.CONFIRMADO
            ):
                continue

            for linea in movimiento.lineas:

                cuenta = cuentas[
                    linea.cuenta.codigo
                ]

                cuenta["cuenta_id"] = linea.cuenta.id
                cuenta["codigo"] = linea.cuenta.codigo
                cuenta["cuenta"] = linea.cuenta.nombre

                if (
                    linea.tipo_afectacion
                    ==
                    TipoAfectacion.DEBITO
                ):

                    cuenta["debitos"] += linea.importe

                else:

                    cuenta["creditos"] += linea.importe

        resultado = []

        for codigo in sorted(
            cuentas.keys(),
        ):

            cuenta = cuentas[codigo]

            saldo = (
                cuenta["debitos"]
                -
                cuenta["creditos"]
            )

            resultado.append(
                {
                    **cuenta,
                    "saldo": saldo,
                }
            )

        return resultado