from __future__ import annotations

from datetime import date
from decimal import Decimal


from pydantic import Field


from domain.enums.tipo_afectacion import TipoAfectacion
from domain.base.entity import Entity
from domain.entities.linea_movimiento import LineaMovimiento

from domain.enums.estado_movimiento import EstadoMovimiento


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
        Calcula la suma de todos los débitos
        del movimiento.
        """

        total = Decimal("0")

        for linea in self.lineas:
            if linea.tipo_afectacion == TipoAfectacion.DEBITO:
                total += linea.importe

        return total
    def total_creditos(self) -> Decimal:
        """
        Calcula la suma de todos los créditos
        del movimiento.
        """

        total = Decimal("0")

        for linea in self.lineas:
            if linea.tipo_afectacion == TipoAfectacion.CREDITO:
                total += linea.importe

        return total
    
    def esta_balanceado(self) -> bool:
        """
        Indica si el movimiento se encuentra
        contablemente balanceado.
        """

        return self.total_debitos() == self.total_creditos()

    def esta_en_borrador(self) -> bool:
        """
        Indica si el movimiento se encuentra en estado BORRADOR.
        """
        return self.estado == EstadoMovimiento.BORRADOR


    def confirmar(self) -> None:
        """
        Confirma el movimiento si cumple todas
        las invariantes del dominio.
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
    def agregar_linea(self, linea: LineaMovimiento) -> None:

        if not self.esta_en_borrador():
            raise ValueError(
                "No se pueden agregar líneas a un movimiento confirmado."
            )

        self.lineas.append(linea)

    