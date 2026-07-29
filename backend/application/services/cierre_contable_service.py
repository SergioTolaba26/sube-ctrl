from datetime import date
from decimal import Decimal

from application.use_cases.estado_resultados.listar_estado_resultados import (
    ListarEstadoResultados,
)

from domain.entities.movimiento import Movimiento
from domain.entities.linea_movimiento import LineaMovimiento


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
        """
        Calcula las líneas necesarias para construir
        el asiento de cierre.
        """

        estado = ListarEstadoResultados(
            self.movimiento_service,
            self.cuenta_service,
        ).execute()

        lineas = []

        #
        # Cancelar ingresos
        #
        for cuenta in estado["ingresos"]:

            saldo = abs(
                cuenta["saldo"],
            )

            if saldo == Decimal("0"):
                continue

            lineas.append(
                {
                    "cuenta_id": cuenta["cuenta_id"],
                    "debito": saldo,
                    "credito": Decimal("0"),
                }
            )

        #
        # Cancelar gastos
        #
        for cuenta in estado["egresos"]:

            if cuenta["saldo"] == Decimal("0"):
                continue

            lineas.append(
                {
                    "cuenta_id": cuenta["cuenta_id"],
                    "debito": Decimal("0"),
                    "credito": cuenta["saldo"],
                }
            )
        # inicio del bloque ha cambiar
        resultado = estado["resultado"]

        #
        # Si no hubo ingresos ni gastos,
        # no hay asiento de cierre.
        #
        if not lineas and resultado == Decimal("0"):
            return []

        cuenta_resultados = None

        for cuenta in self.cuenta_service.listar():

            if cuenta.codigo == "3.2.01":
                cuenta_resultados = cuenta
                break

        if cuenta_resultados is None:
            raise ValueError(
                "No existe la cuenta Resultados Acumulados."
            )

        if resultado > Decimal("0"):

            lineas.append(
                {
                    "cuenta_id": cuenta_resultados.id,
                    "debito": Decimal("0"),
                    "credito": resultado,
                }
            )

        elif resultado < Decimal("0"):

            lineas.append(
                {
                    "cuenta_id": cuenta_resultados.id,
                    "debito": -resultado,
                    "credito": Decimal("0"),
                }
            )

        return lineas

    def generar_asiento_cierre(
        self,
        ejercicio,
    ) -> Movimiento:
        """
        Genera el Movimiento de cierre completo.
        """

        movimiento = Movimiento(
            id=0,
            fecha=date.today(),
            descripcion=f"Cierre ejercicio {ejercicio.anio}",
        )

        lineas = self.calcular_cierre()

        for dato in lineas:

            #
            # Ignorar líneas vacías
            #
            if (
                dato["debito"] == Decimal("0")
                and
                dato["credito"] == Decimal("0")
            ):
                continue

            cuenta = self.cuenta_service.buscar_por_id(
                dato["cuenta_id"],
            )

            if dato["debito"] > Decimal("0"):

                linea = LineaMovimiento.debito(
                    cuenta,
                    dato["debito"],
                )

            elif dato["credito"] > Decimal("0"):

                linea = LineaMovimiento.credito(
                    cuenta,
                    dato["credito"],
                )

            else:
                continue

            movimiento.agregar_linea(
                linea,
            )

        return movimiento