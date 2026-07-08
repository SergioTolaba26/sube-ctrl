from dataclasses import dataclass

from domain.entities.movimiento import Movimiento


@dataclass(slots=True)
class AsientoLibroDiario:
    """
    Representa un asiento del Libro Diario.
    """

    movimiento: Movimiento

    @property
    def fecha(self):
        return self.movimiento.fecha

    