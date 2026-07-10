from domain.enums.tipo_cuenta import TipoCuenta
from domain.services.balance_sumas_saldos import BalanceSumasSaldos
from decimal import Decimal
from domain.value_objects.saldo_cuenta import SaldoCuenta
from domain.enums.tipo_cuenta import TipoCuenta
from domain.value_objects.estado_resultados_calculado import (
    EstadoResultadosCalculado,
)

class EstadoResultados:

    def ingresos(self, movimientos):

        filas = BalanceSumasSaldos().obtener(
            movimientos=movimientos
        )

        return [
            fila
            for fila in filas
            if fila.cuenta.tipo == TipoCuenta.INGRESO
        ]
    
    def gastos(self, movimientos):

        filas = BalanceSumasSaldos().obtener(
            movimientos=movimientos
        )

        return [
            fila
            for fila in filas
            if fila.cuenta.tipo == TipoCuenta.GASTO
        ]
    
    def total_ingresos(self, movimientos):

        return sum(
            (
                fila.saldo
                for fila in self.ingresos(movimientos)
            ),
            Decimal("0")
        )
    
    def total_gastos(self, movimientos):

        return sum(
            (
                fila.saldo
                for fila in self.gastos(movimientos)
            ),
            Decimal("0")
        )
    
    def resultado(self, movimientos):

        return (
            self.total_ingresos(movimientos)
            -
            self.total_gastos(movimientos)
        )
    
    def saldos(
    self,
    movimientos,
):
        """
        Devuelve los saldos acumulados
        de las cuentas de resultado.
        """

        acumulados = {}

        for movimiento in movimientos:

            if not movimiento.esta_confirmado():
                continue

            for linea in movimiento.lineas:

                if linea.cuenta.tipo not in (
                    TipoCuenta.INGRESO,
                    TipoCuenta.GASTO,
                ):
                    continue

                codigo = linea.cuenta.codigo

                if codigo not in acumulados:

                    acumulados[codigo] = SaldoCuenta(
                        cuenta=linea.cuenta,
                        saldo=linea.importe,
                    )

                else:

                    acumulados[codigo].saldo += linea.importe

        return list(acumulados.values())
    
    def calcular(
    self,
    movimientos,
):
        """
        Calcula el Estado de Resultados completo.
        """

        saldos = self.saldos(
            movimientos=movimientos,
        )

        return EstadoResultadosCalculado(
            saldos=saldos,
            resultado=self.resultado(
                movimientos=movimientos,
            ),
        )