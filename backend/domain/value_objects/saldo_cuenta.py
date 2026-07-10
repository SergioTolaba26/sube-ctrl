from decimal import Decimal

from pydantic import BaseModel

from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.enums.tipo_cuenta import TipoCuenta


class SaldoCuenta(BaseModel):

    cuenta: Cuenta
    saldo: Decimal

    def generar_linea_de_cierre(self):
        """
        Genera la línea necesaria para
        cancelar este saldo.
        """

        if self.cuenta.tipo == TipoCuenta.INGRESO:

            return LineaMovimiento.debito(
                cuenta=self.cuenta,
                importe=self.saldo,
            )

        if self.cuenta.tipo == TipoCuenta.GASTO:

            return LineaMovimiento.credito(
                cuenta=self.cuenta,
                importe=self.saldo,
            )

        raise ValueError(
            "Tipo de cuenta no soportado."
        )