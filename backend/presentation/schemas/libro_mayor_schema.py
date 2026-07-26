from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class MovimientoMayorResponse(BaseModel):

    fecha: date

    descripcion: str

    debito: Decimal

    credito: Decimal


class LibroMayorResponse(BaseModel):

    cuenta_id: int

    codigo: str

    cuenta: str

    movimientos: list[
        MovimientoMayorResponse
    ]