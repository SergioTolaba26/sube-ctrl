from decimal import Decimal

from domain.entities.producto import Producto

from domain.repositories.producto_repository import (
    ProductoRepository,
)

from infrastructure.sqlite.base_repository import (
    BaseRepository,
)


class ProductoRepositorySQLite(
    BaseRepository,
    ProductoRepository,
):
    """
    Implementación SQLite del repositorio
    de productos.
    """

    def __init__(
        self,
        connection,
    ):
        super().__init__(
            connection,
        )

    def guardar(
        self,
        producto: Producto,
    ) -> Producto:

        cursor = self._connection.cursor()

        cursor.execute(
            """
            INSERT INTO productos (
                codigo_barras,
                nombre,
                precio_compra,
                activo
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                producto.codigo_barras,
                producto.nombre,
                float(producto.precio_compra),
                int(producto.activo),
            ),
        )

        self._connection.commit()

        producto.id = cursor.lastrowid

        return producto
    def obtener_todos(
        self,
    ) -> list[Producto]:
        raise NotImplementedError


    def buscar_por_id(
        self,
        id_: int,
    ) -> Producto | None:
        raise NotImplementedError


    def buscar_por_codigo_barras(
        self,
        codigo_barras: str,
    ) -> Producto | None:
        raise NotImplementedError


    def eliminar(
        self,
        producto: Producto,
    ) -> None:
        raise NotImplementedError