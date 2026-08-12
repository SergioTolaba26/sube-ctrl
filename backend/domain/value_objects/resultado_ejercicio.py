from decimal import Decimal

from pydantic import BaseModel

from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.enums.tipo_cuenta import TipoCuenta


class ResultadoEjercicio(BaseModel):
    importe: Decimal

    def generar_linea_de_cierre(self):
        cuenta = Cuenta(
            id=None,
            empresa_id=1,
            codigo="3.1.99",
            nombre="Resultado del Ejercicio",
            tipo=TipoCuenta.PATRIMONIO,
        )

        if self.importe > 0:
            return LineaMovimiento.credito(
                cuenta=cuenta,
                importe=self.importe,
            )

        return LineaMovimiento.debito(
            cuenta=cuenta,
            importe=abs(self.importe),
        )