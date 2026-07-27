from decimal import Decimal

from application.use_cases.estado_resultados.listar_estado_resultados import (
    ListarEstadoResultados,
)

from domain.enums.tipo_cuenta import TipoCuenta


class CierreContableService:

    def __init__(
        self,
        movimiento_service,
        cuenta_service,
    ):
        self.movimiento_service = movimiento_service
        self.cuenta_service = cuenta_service

    def calcular_cierre(
        self,
    ):

        estado = ListarEstadoResultados(
            self.movimiento_service,
            self.cuenta_service,
        ).execute()

        cierre = {
            "resultado": estado["resultado"],
            "lineas": [],
        }

        #
        # Cancelar cuentas de ingresos
        #
        for ingreso in estado["ingresos"]:

            cierre["lineas"].append(
                {
                    "cuenta_id": ingreso["cuenta_id"],
                    "codigo": ingreso["codigo"],
                    "nombre": ingreso["cuenta"],
                    "debito": ingreso["creditos"],
                    "credito": Decimal("0"),
                }
            )

        #
        # Cancelar cuentas de gastos
        #
        for gasto in estado["egresos"]:

            cierre["lineas"].append(
                {
                    "cuenta_id": gasto["cuenta_id"],
                    "codigo": gasto["codigo"],
                    "nombre": gasto["cuenta"],
                    "debito": Decimal("0"),
                    "credito": gasto["debitos"],
                }
            )

        #
        # Buscar Resultados Acumulados
        #
        cuenta_resultado = None

        for cuenta in self.cuenta_service.listar():

            if cuenta.codigo == "3.2.01":

                cuenta_resultado = cuenta
                break

        if cuenta_resultado is None:

            raise ValueError(
                "No existe la cuenta Resultados Acumulados."
            )

        resultado = estado["resultado"]

        #
        # Resultado positivo
        #
        if resultado > 0:

            cierre["lineas"].append(
                {
                    "cuenta_id": cuenta_resultado.id,
                    "codigo": cuenta_resultado.codigo,
                    "nombre": cuenta_resultado.nombre,
                    "debito": Decimal("0"),
                    "credito": resultado,
                }
            )

        #
        # Resultado negativo
        #
        elif resultado < 0:

            cierre["lineas"].append(
                {
                    "cuenta_id": cuenta_resultado.id,
                    "codigo": cuenta_resultado.codigo,
                    "nombre": cuenta_resultado.nombre,
                    "debito": abs(resultado),
                    "credito": Decimal("0"),
                }
            )

        return cierre