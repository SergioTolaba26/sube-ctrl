from decimal import Decimal

from domain.enums.tipo_cuenta import (
    TipoCuenta,
)

from domain.services.cuenta_service import (
    CuentaService,
)

from domain.services.movimiento_service import (
    MovimientoService,
)

from application.use_cases.balance_sumas_saldos.listar_balance_sumas_saldos import (
    ListarBalanceSumasSaldos,
)


class ListarEstadoResultados:

    def __init__(
        self,
        movimiento_service: MovimientoService,
        cuenta_service: CuentaService,
    ):
        self.movimiento_service = movimiento_service
        self.cuenta_service = cuenta_service

    def execute(
        self,
    ):

        print("***** ESTADO RESULTADOS NUEVO *****")

        balance = ListarBalanceSumasSaldos(
            self.movimiento_service,
        ).execute()

        resultado = {
            "ingresos": [],
            "egresos": [],
            "total_ingresos": Decimal("0"),
            "total_egresos": Decimal("0"),
            "resultado": Decimal("0"),
        }

        for fila in balance:

            cuenta = self.cuenta_service.buscar_por_id(
                fila["cuenta_id"],
            )

            if cuenta is None:
                continue

            if cuenta.tipo == TipoCuenta.INGRESO:

                resultado["ingresos"].append(
                    fila,
                )

                importe = (
                    fila["creditos"]
                    -
                    fila["debitos"]
                )

                resultado["total_ingresos"] += importe

            elif cuenta.tipo == TipoCuenta.GASTO:

                resultado["egresos"].append(
                    fila,
                )

                importe = (
                    fila["debitos"]
                    -
                    fila["creditos"]
                )

                resultado["total_egresos"] += importe

        resultado["resultado"] = (
            resultado["total_ingresos"]
            -
            resultado["total_egresos"]
        )

        print(resultado)

        return resultado