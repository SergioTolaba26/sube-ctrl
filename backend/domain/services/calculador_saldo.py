from decimal import Decimal

from domain.enums.tipo_afectacion import TipoAfectacion


class CalculadorSaldo:

    def calcular(self, cuenta, movimientos):

        saldo = Decimal("0")

        for movimiento in movimientos:

            if not movimiento.esta_confirmado():
                continue

            for linea in movimiento.lineas:

                if linea.cuenta is not cuenta:
                    continue

                if linea.tipo_afectacion == TipoAfectacion.DEBITO:
                    saldo += linea.importe
                else:
                    saldo -= linea.importe

        return saldo