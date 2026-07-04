from typing import List

from pydantic import Field

from domain.base.entity import Entity
from domain.entities.linea_movimiento import LineaMovimiento


class Movimiento(Entity):
    """
    Representa un hecho del negocio que afecta una o más cuentas.
    """

    descripcion: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Descripción del movimiento."
    )

    lineas: List[LineaMovimiento] = Field(
        default_factory=list,
        description="Líneas que componen el movimiento."
    )

    def agregar_linea(self, linea: LineaMovimiento) -> None:
        """
        Agrega una línea al movimiento.
        """
        self.lineas.append(linea)

    def quitar_linea(self, linea: LineaMovimiento) -> None:
        """
        Elimina una línea del movimiento.
        """
        self.lineas.remove(linea)

    def cantidad_lineas(self) -> int:
        """
        Devuelve la cantidad de líneas.
        """
        return len(self.lineas)

    def validar(self) -> None:
        """
        Valida las reglas básicas del movimiento.
        """
        if self.cantidad_lineas() < 2:
            raise ValueError(
                "Un movimiento debe tener al menos dos líneas."
            )