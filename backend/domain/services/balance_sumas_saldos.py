from decimal import Decimal

from domain.enums.tipo_afectacion import TipoAfectacion
from domain.services.fila_balance_sumas_saldos import (
    FilaBalanceSumasSaldos,
)

class BalanceSumasSaldos:

    def obtener(self, movimientos):

        filas = {}

        for movimiento in movimientos:

            if not movimiento.esta_confirmado():
                continue

            for linea in movimiento.lineas:

                codigo = linea.cuenta.codigo

                if codigo not in filas:
                    filas[codigo] = FilaBalanceSumasSaldos(
                        cuenta=linea.cuenta
                    )
                if linea.tipo_afectacion == TipoAfectacion.DEBITO:
                    filas[codigo].total_debitos += linea.importe
                else:
                    filas[codigo].total_creditos += linea.importe

        return list(filas.values())
    
