from domain.enums.tipo_cuenta import TipoCuenta
from domain.services.balance_sumas_saldos import BalanceSumasSaldos
from decimal import Decimal

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