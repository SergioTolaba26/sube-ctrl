from domain.enums.tipo_cuenta import TipoCuenta
from domain.services.balance_sumas_saldos import BalanceSumasSaldos
from decimal import Decimal

class BalanceGeneral:

    def activos(self, movimientos):
        filas = BalanceSumasSaldos().obtener(
            movimientos=movimientos
        )

        return [
            fila
            for fila in filas
            if fila.cuenta.tipo == TipoCuenta.ACTIVO
        ]

    def pasivos(self, movimientos):
        filas = BalanceSumasSaldos().obtener(
            movimientos=movimientos
        )

        return [
            fila
            for fila in filas
            if fila.cuenta.tipo == TipoCuenta.PASIVO
        ]

    def patrimonio(self, movimientos):
        filas = BalanceSumasSaldos().obtener(
            movimientos=movimientos
        )

        return [
            fila
            for fila in filas
            if fila.cuenta.tipo == TipoCuenta.PATRIMONIO
        ]
    
    def total_activos(self, movimientos):

        return sum(
            (
                fila.saldo
                for fila in self.activos(movimientos)
            ),
            Decimal("0")
        )
    
    def total_pasivos(self, movimientos):

        return sum(
            (
                fila.saldo
                for fila in self.pasivos(movimientos)
            ),
            Decimal("0")
        )
    
    def total_patrimonio(self, movimientos):

        return sum(
            (
                fila.saldo
                for fila in self.patrimonio(movimientos)
            ),
            Decimal("0")
        )