from dataclasses import dataclass
from decimal import Decimal


from domain.entities.linea_movimiento import LineaMovimiento


@dataclass(slots=True, frozen=True)
class RenglonLibroMayor:
    """
    Representa un renglón del Libro Mayor.

    Es una vista del dominio construida a partir de una
    Línea de Movimiento y el saldo acumulado hasta ese momento.
    """

    linea: LineaMovimiento
    saldo: Decimal

    @property
    def cuenta(self):
        return self.linea.cuenta
    @property
    def importe(self):
        return self.linea.importe
    @property
    def movimiento(self):
        return self.linea.movimiento