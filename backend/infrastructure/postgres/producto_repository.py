
import psycopg

from decimal import Decimal

from domain.entities.producto import Producto

from domain.errors.producto_duplicado_error import (
    ProductoDuplicadoError,
)

from domain.repositories.producto_repository import (
    ProductoRepository,
)


class ProductoRepositoryPostgres(
    ProductoRepository,
):

    def __init__(
        self,
        connection,
    ):
        self._connection = connection

    # =========================================================
    # GUARDAR
    # =========================================================

    def guardar(
        self,
        producto: Producto,
    ) -> Producto:

        try:

            with self._connection.cursor() as cursor:

                if producto.id is None:

                    cursor.execute(
                        """
                        INSERT INTO productos (
                            empresa_id,
                            codigo_barras,
                            nombre,
                            precio_compra,
                            activo
                        )
                        VALUES (
                            %s,
                            %s,
                            %s,
                            %s,
                            %s
                        )
                        RETURNING id
                        """,
                        (
                            producto.empresa_id,
                            producto.codigo_barras,
                            producto.nombre,
                            producto.precio_compra,
                            producto.activo,
                        ),
                    )

                    producto.id = cursor.fetchone()[0]

                else:

                    cursor.execute(
                        """
                        INSERT INTO productos (
                            id,
                            empresa_id,
                            codigo_barras,
                            nombre,
                            precio_compra,
                            activo
                        )
                        VALUES (
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s
                        )
                        ON CONFLICT (id)
                        DO UPDATE SET
                            empresa_id = EXCLUDED.empresa_id,
                            codigo_barras = EXCLUDED.codigo_barras,
                            nombre = EXCLUDED.nombre,
                            precio_compra = EXCLUDED.precio_compra,
                            activo = EXCLUDED.activo
                        """,
                        (
                            producto.id,
                            producto.empresa_id,
                            producto.codigo_barras,
                            producto.nombre,
                            producto.precio_compra,
                            producto.activo,
                        ),
                    )

            self._connection.commit()

        except psycopg.errors.UniqueViolation as exc:

            self._connection.rollback()

            raise ProductoDuplicadoError(
                "Ya existe un producto con ese código de barras."
            ) from exc

        return producto

    # =========================================================
    # LISTAR
    # =========================================================

    def listar(
        self,
        empresa_id: int,
    ) -> list[Producto]:

        with self._connection.cursor() as cursor:

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
                WHERE empresa_id = %s
                ORDER BY nombre
                """,
                (
                    empresa_id,
                ),
            )

            filas = cursor.fetchall()

        return [
            self._fila_a_producto(
                fila,
            )
            for fila in filas
        ]

    # =========================================================
    # BUSCAR POR ID
    # =========================================================

    def buscar_por_id(
        self,
        empresa_id: int,
        producto_id: int,
    ) -> Producto | None:

        with self._connection.cursor() as cursor:

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
                WHERE empresa_id = %s
                  AND id = %s
                """,
                (
                    empresa_id,
                    producto_id,
                ),
            )

            fila = cursor.fetchone()

        if fila is None:
            return None

        return self._fila_a_producto(
            fila,
        )

    # =========================================================
    # BUSCAR POR CÓDIGO DE BARRAS
    # =========================================================

    def buscar_por_codigo_barras(
        self,
        empresa_id: int,
        codigo_barras: str,
    ) -> Producto | None:

        with self._connection.cursor() as cursor:

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
                WHERE empresa_id = %s
                  AND codigo_barras = %s
                """,
                (
                    empresa_id,
                    codigo_barras,
                ),
            )

            fila = cursor.fetchone()

        if fila is None:
            return None

        return self._fila_a_producto(
            fila,
        )

    # =========================================================
    # MODIFICAR
    # =========================================================

    def modificar(
        self,
        producto: Producto,
    ) -> Producto | None:

        try:

            with self._connection.cursor() as cursor:

                cursor.execute(
                    """
                    UPDATE productos
                    SET
                        empresa_id = %s,
                        codigo_barras = %s,
                        nombre = %s,
                        precio_compra = %s,
                        activo = %s
                    WHERE empresa_id = %s
                      AND id = %s
                    """,
                    (
                        producto.empresa_id,
                        producto.codigo_barras,
                        producto.nombre,
                        producto.precio_compra,
                        producto.activo,
                        producto.empresa_id,
                        producto.id,
                    ),
                )

                if cursor.rowcount == 0:

                    self._connection.rollback()

                    return None

            self._connection.commit()

        except psycopg.errors.UniqueViolation as exc:

            self._connection.rollback()

            raise ProductoDuplicadoError(
                "Ya existe un producto con ese código de barras."
            ) from exc

        return producto

    # =========================================================
    # ELIMINAR
    # =========================================================

    def eliminar(
        self,
        empresa_id: int,
        producto_id: int,
    ) -> bool:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                DELETE FROM productos
                WHERE empresa_id = %s
                  AND id = %s
                """,
                (
                    empresa_id,
                    producto_id,
                ),
            )

            eliminado = cursor.rowcount > 0

        self._connection.commit()

        return eliminado

    # =========================================================
    # MAPPER INTERNO
    # =========================================================

    @staticmethod
    def _fila_a_producto(
        fila,
    ) -> Producto:

        return Producto(

            id=fila[0],

            empresa_id=fila[1],

            codigo_barras=fila[2],

            nombre=fila[3],

            precio_compra=Decimal(
                str(fila[4]),
            ),

            activo=fila[5],
        )
