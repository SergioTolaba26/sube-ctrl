from decimal import Decimal

from domain.enums.tipo_afectacion import TipoAfectacion
from domain.enums.tipo_cuenta import TipoCuenta


class CalculadorSaldo:

    def calcular(self, cuenta, movimientos):

        saldo = Decimal("0")

        for movimiento in movimientos:

            if not movimiento.esta_confirmado():
                continue

            for linea in movimiento.lineas:

                if linea.cuenta is not cuenta:
                    continue

                # if cuenta.tipo in (
                #     TipoCuenta.ACTIVO,
                #     TipoCuenta.GASTO,
                # ):
                if cuenta.tipo.es_naturaleza_deudora(): # if cuenta.es_naturaleza_deudora(): #saldo += cuenta.efecto(linea)
                    if linea.tipo_afectacion == TipoAfectacion.DEBITO:
                        saldo += linea.importe
                    else:
                        saldo -= linea.importe

                else:
                    if linea.tipo_afectacion == TipoAfectacion.DEBITO:
                        saldo -= linea.importe
                    else:
                        saldo += linea.importe

        return saldo