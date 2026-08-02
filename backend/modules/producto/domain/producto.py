"""
Entidad de dominio Producto.

Este módulo define la entidad principal del dominio Producto.

La entidad no conoce:
- Base de datos
- API REST
- HTML
- JavaScript
- SQLite
- FastAPI

Su única responsabilidad es representar un Producto dentro del dominio.
"""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True)
class Producto:
    """
    Entidad de dominio que representa un producto.
    """

    codigo_barras: str
    nombre: str
    precio_compra: Decimal