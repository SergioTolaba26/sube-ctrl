from decimal import Decimal

from pydantic import BaseModel

from domain.entities.linea_movimiento import LineaMovimiento
from domain.enums.tipo_afectacion import TipoAfectacion
from tests.builders.entidades_builder import crear_resultado_del_ejercicio

class ResultadoEjercicio(BaseModel):

    importe: Decimal

    def generar_linea_de_cierre(self):

        cuenta = crear_resultado_del_ejercicio()

        if self.importe > 0:

            return LineaMovimiento.credito(
                cuenta=cuenta,
                importe=self.importe,
            )

        return LineaMovimiento.debito(
            cuenta=cuenta,
            importe=abs(self.importe),
        )