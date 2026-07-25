from __future__ import annotations

from datetime import date
from decimal import Decimal

from pydantic import Field

from domain.base.entity import Entity
from domain.entities.linea_movimiento import LineaMovimiento
from domain.enums.estado_movimiento import EstadoMovimiento
from domain.enums.tipo_afectacion import TipoAfectacion


class Movimiento(Entity):
    """
    Representa el registro de un hecho económico.

    Es el Aggregate Root responsable de mantener la consistencia
    de todas las afectaciones producidas por ese hecho.
    """

    estado: EstadoMovimiento = Field(
        default=EstadoMovimiento.BORRADOR,
        description="Estado actual del movimiento."
    )

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

        if not self.esta_en_borrador():
            raise ValueError(
                "No se pueden agregar líneas a un movimiento confirmado."
            )

        if not linea.cuenta.esta_activa():
            raise ValueError(
                "La cuenta está inactiva."
            )

        if not linea.cuenta.es_imputable():
            raise ValueError(
                "La cuenta es no imputable."
            )

        # La línea pasa a pertenecer a este movimiento.
        linea.movimiento = self

        self.lineas.append(linea)
    def cantidad_lineas(self) -> int:
        """
        Devuelve la cantidad de líneas del movimiento.
        """
        return len(self.lineas)

    def tiene_lineas(self) -> bool:
        """
        Indica si el movimiento posee al menos una línea.
        """
        return self.cantidad_lineas() > 0

    def total_debitos(self) -> Decimal:
        """
        Calcula la suma de todos los débitos.
        """
        total = Decimal("0")

        for linea in self.lineas:
            if linea.tipo_afectacion == TipoAfectacion.DEBITO:
                total += linea.importe

        return total

    def total_creditos(self) -> Decimal:
        """
        Calcula la suma de todos los créditos.
        """
        total = Decimal("0")

        for linea in self.lineas:
            if linea.tipo_afectacion == TipoAfectacion.CREDITO:
                total += linea.importe

        return total

    def esta_balanceado(self) -> bool:
        """
        Indica si el movimiento está balanceado.
        """
        return self.total_debitos() == self.total_creditos()

    def esta_en_borrador(self) -> bool:
        """
        Indica si el movimiento está en estado BORRADOR.
        """
        return self.estado == EstadoMovimiento.BORRADOR
    

    def esta_confirmado(self) -> bool:
        """
        Indica si el movimiento se encuentra en estado CONFIRMADO.
        """
        return self.estado == EstadoMovimiento.CONFIRMADO

    def confirmar(self) -> None:
        """
        Confirma el movimiento.
        """

        if not self.esta_en_borrador():
            raise ValueError(
                "Solo un movimiento en borrador puede confirmarse."
            )

        if not self.tiene_lineas():
            raise ValueError(
                "No se puede confirmar un movimiento sin líneas."
            )

        if not self.esta_balanceado():
            raise ValueError(
                "El movimiento no está balanceado."
            )

        self.estado = EstadoMovimiento.CONFIRMADO

    def cambiar_descripcion(self, descripcion: str) -> None:
        """
        Cambia la descripción del movimiento.
        """

        if not self.esta_en_borrador():
            raise ValueError(
                "No se puede modificar un movimiento confirmado."
            )

        self.descripcion = descripcion

    def anular(self) -> None:
        """
        Anula un movimiento previamente confirmado.
        """

        if self.estado != EstadoMovimiento.CONFIRMADO:
            raise ValueError(
                "Solo un movimiento confirmado puede anularse."
            )

        self.estado = EstadoMovimiento.ANULADO

    def eliminar_linea(
        self,
        indice: int,
    ) -> None:

        if not self.esta_en_borrador():
            raise ValueError(
                "No se pueden eliminar líneas de un movimiento confirmado."
            )

        if indice < 0 or indice >= len(self.lineas):
            raise IndexError(
                "Línea inexistente."
            )

        self.lineas.pop(indice)