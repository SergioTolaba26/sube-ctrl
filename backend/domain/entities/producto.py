from decimal import Decimal

from pydantic import Field

from domain.base.entity import Entity


class Producto(Entity):
    """
    Entidad del dominio que representa un producto.
    """

    codigo_barras: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )

    nombre: str = Field(
        ...,
        min_length=1,
        max_length=150,
    )

    precio_compra: Decimal = Field(
        ...,
        ge=0,
    )

    activo: bool = Field(
        default=True,
    )

    def activar(self) -> None:
        """
        Activa el producto.
        """
        self.activo = True

    def desactivar(self) -> None:
        """
        Desactiva el producto.
        """
        self.activo = False