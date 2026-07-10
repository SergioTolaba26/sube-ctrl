from decimal import Decimal

from pydantic import BaseModel

from domain.value_objects.saldo_cuenta import SaldoCuenta


class EstadoResultadosCalculado(BaseModel):

    saldos: list[SaldoCuenta]

    resultado: Decimal
    def calcular(self, movimientos):

        saldos = self.saldos(movimientos)

        return EstadoResultadosCalculado(
            saldos=saldos,
            resultado=self.resultado(movimientos),
        )