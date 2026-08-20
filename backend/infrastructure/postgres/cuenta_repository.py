import psycopg

from domain.entities.cuenta import Cuenta

from domain.enums.tipo_cuenta import TipoCuenta


class CuentaRepositoryPostgres:

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
        cuenta: Cuenta,
    ) -> None:

        with self._connection.cursor() as cursor:

            if cuenta.id is None:

                cursor.execute(
                    """
                    INSERT INTO cuentas (
                        empresa_id,
                        codigo,
                        nombre,
                        tipo,
                        activa,
                        imputable
                    )
                    VALUES (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                    RETURNING id
                    """,
                    (
                        cuenta.empresa_id,
                        cuenta.codigo,
                        cuenta.nombre,
                        cuenta.tipo.name,
                        cuenta.activa,
                        cuenta.imputable,
                    ),
                )

                cuenta.id = cursor.fetchone()[0]

            else:

                cursor.execute(
                    """
                    INSERT INTO cuentas (
                        id,
                        empresa_id,
                        codigo,
                        nombre,
                        tipo,
                        activa,
                        imputable
                    )
                    VALUES (
                        %s,
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
                        codigo = EXCLUDED.codigo,
                        nombre = EXCLUDED.nombre,
                        tipo = EXCLUDED.tipo,
                        activa = EXCLUDED.activa,
                        imputable = EXCLUDED.imputable
                    """,
                    (
                        cuenta.id,
                        cuenta.empresa_id,
                        cuenta.codigo,
                        cuenta.nombre,
                        cuenta.tipo.name,
                        cuenta.activa,
                        cuenta.imputable,
                    ),
                )

        self._connection.commit()
    # =========================================================
    # LISTAR
    # =========================================================

    def listar(
        self,
        empresa_id: int,
    ) -> list[Cuenta]:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    id,
                    empresa_id,
                    codigo,
                    nombre,
                    tipo,
                    activa,
                    imputable
                FROM cuentas
                WHERE empresa_id = %s
                ORDER BY id
                """,
                (
                    empresa_id,
                ),
            )

            filas = cursor.fetchall()

        return [
            self._fila_a_cuenta(
                fila,
            )
            for fila in filas
        ]

    # =========================================================
    # OBTENER TODAS
    #
    # Compatibilidad con posibles usos existentes.
    # =========================================================

    def obtener_todas(
        self,
        empresa_id: int,
    ) -> list[Cuenta]:

        return self.listar(
            empresa_id,
        )

    # =========================================================
    # BUSCAR POR ID
    # =========================================================

    def buscar_por_id(
        self,
        empresa_id: int,
        cuenta_id: int,
    ) -> Cuenta | None:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    id,
                    empresa_id,
                    codigo,
                    nombre,
                    tipo,
                    activa,
                    imputable
                FROM cuentas
                WHERE empresa_id = %s
                  AND id = %s
                """,
                (
                    empresa_id,
                    cuenta_id,
                ),
            )

            fila = cursor.fetchone()

        if fila is None:
            return None

        return self._fila_a_cuenta(
            fila,
        )

    # =========================================================
    # BUSCAR POR CODIGO
    # =========================================================

    def buscar_por_codigo(
        self,
        empresa_id: int,
        codigo: str,
    ) -> Cuenta | None:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    id,
                    empresa_id,
                    codigo,
                    nombre,
                    tipo,
                    activa,
                    imputable
                FROM cuentas
                WHERE empresa_id = %s
                  AND codigo = %s
                """,
                (
                    empresa_id,
                    codigo,
                ),
            )

            fila = cursor.fetchone()

        if fila is None:
            return None

        return self._fila_a_cuenta(
            fila,
        )

    # =========================================================
    # MODIFICAR
    # =========================================================

    def modificar(
        self,
        empresa_id: int,
        cuenta: Cuenta,
    ) -> Cuenta | None:

        cuenta_actual = self.buscar_por_id(
            empresa_id,
            cuenta.id,
        )

        if cuenta_actual is None:
            return None

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                UPDATE cuentas
                SET
                    codigo = %s,
                    nombre = %s,
                    tipo = %s,
                    activa = %s,
                    imputable = %s
                WHERE empresa_id = %s
                  AND id = %s
                """,
                (
                    cuenta.codigo,
                    cuenta.nombre,
                    cuenta.tipo.name,
                    cuenta.activa,
                    cuenta.imputable,
                    empresa_id,
                    cuenta.id,
                ),
            )

        self._connection.commit()

        return cuenta

    # =========================================================
    # ELIMINAR
    # =========================================================

    def eliminar(
        self,
        empresa_id: int,
        cuenta_id: int,
    ) -> Cuenta | None:

        cuenta = self.buscar_por_id(
            empresa_id,
            cuenta_id,
        )

        if cuenta is None:
            return None

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                DELETE FROM cuentas
                WHERE empresa_id = %s
                  AND id = %s
                """,
                (
                    empresa_id,
                    cuenta_id,
                ),
            )

        self._connection.commit()

        return cuenta

    # =========================================================
    # MAPPER INTERNO
    # =========================================================

    @staticmethod
    def _fila_a_cuenta(
        fila,
    ) -> Cuenta:

        return Cuenta(

            id=fila[0],

            empresa_id=fila[1],

            codigo=fila[2],

            nombre=fila[3],

            tipo=TipoCuenta[
                fila[4]
            ],

            activa=fila[5],

            imputable=fila[6],
        )