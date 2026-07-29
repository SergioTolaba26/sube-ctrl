from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class LineaAsientoRequest(
    BaseModel,
):

    cuenta_id: int

    debito: Decimal = Decimal("0")

    credito: Decimal = Decimal("0")


class RegistrarAsientoRequest(
    BaseModel,
):

    fecha: date

    descripcion: str

    lineas: list[
        LineaAsientoRequest
    ]