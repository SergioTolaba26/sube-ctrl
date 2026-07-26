from decimal import Decimal

from application.use_cases.balance_sumas_saldos.listar_balance_sumas_saldos import (
    ListarBalanceSumasSaldos,
)

from application.use_cases.estado_resultados.listar_estado_resultados import (
    ListarEstadoResultados,
)

from domain.enums.tipo_cuenta import (
    TipoCuenta,
)


class ListarBalanceGeneral:

    def __init__(
        self,
        movimiento_service,
        cuenta_service,
    ):
        self.movimiento_service = movimiento_service
        self.cuenta_service = cuenta_service

    def execute(
        self,
    ):

        balance = ListarBalanceSumasSaldos(
            self.movimiento_service,
        ).execute()

        estado_resultados = ListarEstadoResultados(
            self.movimiento_service,
            self.cuenta_service,
        ).execute()

        resultado = {
            "activos": [],
            "pasivos": [],
            "patrimonio": [],
            "total_activo": Decimal("0"),
            "total_pasivo": Decimal("0"),
            "total_patrimonio": Decimal("0"),
            "resultado_ejercicio": estado_resultados["resultado"],
            "total_pasivo_patrimonio": Decimal("0"),
            "pasivo_mas_patrimonio": Decimal("0"),
            "diferencia": Decimal("0"),
        }

        for fila in balance:

            cuenta = self.cuenta_service.buscar_por_id(
                fila["cuenta_id"],
            )

            if cuenta is None:
                continue

            saldo = fila["saldo"]

            if cuenta.tipo == TipoCuenta.ACTIVO:

                resultado["activos"].append(
                    fila,
                )

                resultado["total_activo"] += saldo

            elif cuenta.tipo == TipoCuenta.PASIVO:

                resultado["pasivos"].append(
                    fila,
                )

                resultado["total_pasivo"] += abs(
                    saldo,
                )

            elif cuenta.tipo == TipoCuenta.PATRIMONIO:

                resultado["patrimonio"].append(
                    fila,
                )

                resultado["total_patrimonio"] += abs(
                    saldo,
                )

        # El resultado del ejercicio forma parte del patrimonio
        resultado["total_patrimonio"] += (
            resultado["resultado_ejercicio"]
        )

        resultado["pasivo_mas_patrimonio"] = (
            resultado["total_pasivo"]
            +
            resultado["total_patrimonio"]
        )

        resultado["total_pasivo_patrimonio"] = (
            resultado["pasivo_mas_patrimonio"]
        )

        resultado["diferencia"] = (
            resultado["total_activo"]
            -
            resultado["pasivo_mas_patrimonio"]
        )

        return resultado