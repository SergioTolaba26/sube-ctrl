"""
Entidad de dominio Producto.

Representa un producto dentro del dominio del sistema.

El dominio no conoce:
- SQLite
- FastAPI
- HTML
- JavaScript

Su responsabilidad es garantizar que un Producto
siempre exista en un estado válido.
"""

from dataclasses import dataclass
from decimal import Decimal

from backend.modules.producto.exceptions.producto_exception import (
    ProductoInvalidoError,
)

@dataclass(slots=True)
class Producto:
    """
    Entidad de dominio Producto.
    """

    codigo_barras: str
    nombre: str
    precio_compra: Decimal

    def __post_init__(self) -> None:
        """
        Valida las reglas del dominio inmediatamente
        después de crear la entidad.
        """

        self.codigo_barras = self.codigo_barras.strip()
        self.nombre = self.nombre.strip()

        if not self.codigo_barras:
            raise ProductoInvalidoError("El código de barras es obligatorio.")

        if not self.nombre:
            raise ProductoInvalidoError("El nombre es obligatorio.")

        if self.precio_compra <= Decimal("0"):
            raise ProductoInvalidoError(
                "El precio de compra debe ser mayor que cero."
            )