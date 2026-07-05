from __future__ import annotations

from datetime import date

from pydantic import Field

from domain.base.entity import Entity
from domain.entities.linea_movimiento import LineaMovimiento


class Movimiento(Entity):
    """
    Representa el registro de un hecho económico.

    Es el Aggregate Root responsable de mantener la consistencia
    de todas las afectaciones producidas por ese hecho.
    """

    fecha: date = Field(
        ...,
        description="Fecha del hecho económico."
    )

    descripcion: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Descripción del hecho económico."
    )

    lineas: list[LineaMovimiento] = Field(
        default_factory=list,
        description="Líneas que componen el movimiento."
    )
    def agregar_linea(self, linea: LineaMovimiento) -> None:
        """
        Agrega una línea al movimiento.
        """
        self.lineas.append(linea) 

    def cantidad_lineas(self) -> int:
        """
        Devuelve la cantidad de líneas del movimiento.
        """
        return len(self.lineas)   