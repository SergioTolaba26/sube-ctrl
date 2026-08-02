"""
Módulo: producto.py

Define la entidad Producto del dominio.

La entidad representa un producto del sistema independientemente
de cómo se almacene o se exponga mediante una API.

No contiene lógica de base de datos.
No contiene lógica HTTP.
No depende de SQLite.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass(slots=True)
class Producto:
    """
    Representa un producto comercializado por el sistema.
    """

    codigo_barras: str
    nombre: str
    precio_compra: Decimal

    id: Optional[int] = None