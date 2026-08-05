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
    def _row_to_producto(
        self,
        fila,
    ) -> Producto:

        return Producto(
            id=fila["id"],
            codigo_barras=fila["codigo_barras"],
            nombre=fila["nombre"],
            precio_compra=Decimal(
                str(fila["precio_compra"])
            ),
            activo=bool(
                fila["activo"],
            ),
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
    
    def buscar_por_codigo_barras(
        self,
        codigo_barras: str,
    ) -> Producto | None:

        cursor = self._connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                codigo_barras,
                nombre,
                precio_compra,
                activo
            FROM productos
            WHERE codigo_barras = ?
            """,
            (
                codigo_barras,
            ),
        )

        fila = cursor.fetchone()

        if fila is None:
            return None

        return self._row_to_producto(
            fila,
    )

    def eliminar(
        self,
        producto: Producto,
    ) -> None:
        raise NotImplementedError
    
    def buscar_por_id(
        self,
        producto_id: int,
    ) -> Producto | None:

        cursor = self._connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                codigo_barras,
                nombre,
                precio_compra,
                activo
            FROM productos
            WHERE id = ?
            """,
            (
                producto_id,
            ),
        )

        fila = cursor.fetchone()

        if fila is None:
            return None

        return self._row_to_producto(
            fila,
        )
    
    def obtener_todos(
        self,
    ) -> list[Producto]:

        cursor = self._connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                codigo_barras,
                nombre,
                precio_compra,
                activo
            FROM productos
            ORDER BY nombre
            """
        )

        filas = cursor.fetchall()

        return [
            self._row_to_producto(
                fila,
            )
            for fila in filas
        ]
    
    def actualizar(
        self,
        producto: Producto,
    ) -> Producto | None:

        cursor = self._connection.cursor()

        cursor.execute(
            """
            UPDATE productos
            SET
                codigo_barras = ?,
                nombre = ?,
                precio_compra = ?,
                activo = ?
            WHERE id = ?
            """,
            (
                producto.codigo_barras,
                producto.nombre,
                float(
                    producto.precio_compra,
                ),
                int(
                    producto.activo,
                ),
                producto.id,
            ),
        )
        self._connection.commit()

        if cursor.rowcount == 0:
            return None
        return producto
    
    def eliminar(
        self,
        producto_id: int,
    ) -> bool:

        cursor = self._connection.cursor()
        cursor.execute(
            """
            DELETE FROM productos
            WHERE id = ?
            """,
            (
                producto_id,
            ),
        )
        # Lo confirmo
        self._connection.commit()
        # Verifico que se eliminó el registro
        return cursor.rowcount > 0