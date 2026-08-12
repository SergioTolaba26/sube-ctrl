from decimal import Decimal
import sqlite3

from domain.entities.producto import Producto

from domain.repositories.producto_repository import (
    ProductoRepository,
)

from infrastructure.sqlite.base_repository import (
    BaseRepository,
)
from domain.errors.producto_duplicado_error import (
    ProductoDuplicadoError,
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
            empresa_id=fila["empresa_id"],
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

        try:

            cursor.execute(
                """
                INSERT INTO productos (
                    empresa_id,
                    codigo_barras,
                    nombre,
                    precio_compra,
                    activo
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    producto.empresa_id,
                    producto.codigo_barras,
                    producto.nombre,
                    float(producto.precio_compra),
                    int(producto.activo),
                ),
            )

            self._connection.commit()

        except sqlite3.IntegrityError as exc:

            raise ProductoDuplicadoError(
                "Ya existe un producto con ese código de barras."
            ) from exc

        producto.id = cursor.lastrowid

        return producto

    def buscar_por_codigo_barras(
        self,
        empresa_id: int,
        codigo_barras: str,
    ) -> Producto | None:

        cursor = self._connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                empresa_id,
                codigo_barras,
                nombre,
                precio_compra,
                activo
            FROM productos
            WHERE empresa_id = ?
            AND codigo_barras = ?
            """,
            (
                empresa_id,
                codigo_barras,
            ),
        )

        fila = cursor.fetchone()

        if fila is None:
            return None

        return self._row_to_producto(
            fila,
        )
    
    def buscar_por_id(
        self,
        empresa_id: int,
        producto_id: int,
    ) -> Producto | None:

        cursor = self._connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                empresa_id,
                codigo_barras,
                nombre,
                precio_compra,
                activo
            FROM productos
            WHERE empresa_id = ?
            AND id = ?
            """,
            (
                empresa_id,
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
        empresa_id: int,
    ) -> list[Producto]:

        cursor = self._connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                empresa_id,
                codigo_barras,
                nombre,
                precio_compra,
                activo
            FROM productos
            WHERE empresa_id = ?
            ORDER BY nombre
            """,
            (
                empresa_id,
            ),
        )

        filas = cursor.fetchall()

        return [
            self._row_to_producto(
                fila,
            )
            for fila in filas
        ]
    
    def modificar(
        self,
        producto: Producto,
    ) -> Producto | None:

        cursor = self._connection.cursor()

        cursor.execute(
            """
            UPDATE productos
            SET
                empresa_id = ?,
                codigo_barras = ?,
                nombre = ?,
                precio_compra = ?,
                activo = ?
            WHERE id = ?
            """,
            (
                producto.empresa_id,
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
        empresa_id: int,
        producto_id: int,
    ) -> bool:

        cursor = self._connection.cursor()

        cursor.execute(
            """
            DELETE FROM productos
            WHERE empresa_id = ?
            AND id = ?
            """,
            (
                empresa_id,
                producto_id,
            ),
        )

        self._connection.commit()

        return cursor.rowcount > 0