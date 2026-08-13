from __future__ import annotations

from datetime import date

from pydantic import Field

from domain.base.entity import Entity

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)


class Ejercicio(Entity):

    empresa_id: int = Field(
        ...,
        description="Empresa a la que pertenece el ejercicio.",
    )

    anio: int

    fecha_apertura: date

    fecha_cierre: date | None = None

    estado: EstadoEjercicio = (
        EstadoEjercicio.ABIERTO
    )

    def cerrar(self):

        if self.estado == EstadoEjercicio.CERRADO:
            raise ValueError(
                "El ejercicio ya está cerrado."
            )

        self.estado = EstadoEjercicio.CERRADO
        self.fecha_cierre = date.today()

    def abrir(self):
        """
        Reabre un ejercicio previamente cerrado.
        """

        if self.estado == EstadoEjercicio.ABIERTO:
            raise ValueError(
                "El ejercicio ya está abierto."
            )

        self.estado = EstadoEjercicio.ABIERTO
        self.fecha_cierre = None

    def esta_cerrado(
        self,
    ) -> bool:

        return (
            self.estado
            == EstadoEjercicio.CERRADO
        )