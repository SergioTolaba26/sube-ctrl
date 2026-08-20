import psycopg

from domain.entities.empresa import Empresa

from domain.repositories.empresa_repository import (
    EmpresaRepository,
)


class EmpresaRepositoryPostgres(
    EmpresaRepository,
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
        empresa: Empresa,
    ) -> None:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO empresas (
                    id,
                    razon_social,
                    nombre_fantasia,
                    cuit,
                    activa
                )
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
                ON CONFLICT (id)
                DO UPDATE SET
                    razon_social = EXCLUDED.razon_social,
                    nombre_fantasia = EXCLUDED.nombre_fantasia,
                    cuit = EXCLUDED.cuit,
                    activa = EXCLUDED.activa
                """,
                (
                    empresa.id,
                    empresa.razon_social,
                    empresa.nombre_fantasia,
                    empresa.cuit,
                    empresa.activa,
                ),
            )

        self._connection.commit()

    # =========================================================
    # LISTAR
    # =========================================================

    def listar(
        self,
    ) -> list[Empresa]:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    id,
                    razon_social,
                    nombre_fantasia,
                    cuit,
                    activa
                FROM empresas
                ORDER BY id
                """
            )

            filas = cursor.fetchall()

        return [
            self._fila_a_empresa(
                fila,
            )
            for fila in filas
        ]

    # =========================================================
    # OBTENER TODAS
    #
    # Compatibilidad con el contrato actual
    # =========================================================

    def obtener_todas(
        self,
    ) -> list[Empresa]:

        return self.listar()

    # =========================================================
    # BUSCAR POR ID
    # =========================================================

    def buscar_por_id(
        self,
        empresa_id: int,
    ) -> Empresa | None:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    id,
                    razon_social,
                    nombre_fantasia,
                    cuit,
                    activa
                FROM empresas
                WHERE id = %s
                """,
                (
                    empresa_id,
                ),
            )

            fila = cursor.fetchone()

        if fila is None:
            return None

        return self._fila_a_empresa(
            fila,
        )

    # =========================================================
    # BUSCAR POR CUIT
    # =========================================================

    def buscar_por_cuit(
        self,
        cuit: str,
    ) -> Empresa | None:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    id,
                    razon_social,
                    nombre_fantasia,
                    cuit,
                    activa
                FROM empresas
                WHERE cuit = %s
                """,
                (
                    cuit,
                ),
            )

            fila = cursor.fetchone()

        if fila is None:
            return None

        return self._fila_a_empresa(
            fila,
        )

    # =========================================================
    # ELIMINAR
    #
    # Aceptamos el id porque así lo utiliza actualmente
    # EliminarEmpresa y EmpresaService.
    # =========================================================

    def eliminar(
        self,
        empresa_id,
    ) -> None:

        if isinstance(
            empresa_id,
            Empresa,
        ):
            empresa_id = empresa_id.id

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                DELETE FROM empresas
                WHERE id = %s
                """,
                (
                    empresa_id,
                ),
            )

        self._connection.commit()

    # ===to======================================================
    # MODIFICAR
    #
    # Actualmente ModificarEmpresa utiliza guardar(),
    # por lo que no necesitamos usar este método todavía.
    # =========================================================

    def modificar(
        self,
        empresa: Empresa,
    ) -> Empresa | None:

        self.guardar(
            empresa,
        )

        return empresa

    # =========================================================
    # MAPPER INTERNO
    # =========================================================

    @staticmethod
    def _fila_a_empresa(
        fila,
    ) -> Empresa:

        return Empresa(
            id=fila[0],
            razon_social=fila[1],
            nombre_fantasia=fila[2],
            cuit=fila[3],
            activa=fila[4],
        )