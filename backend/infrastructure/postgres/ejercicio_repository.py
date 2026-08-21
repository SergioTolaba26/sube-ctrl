from domain.entities.ejercicio import (
    Ejercicio,
)

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)


class EjercicioRepositoryPostgres:

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
        ejercicio: Ejercicio,
    ) -> None:

        with self._connection.cursor() as cursor:

            if ejercicio.id is None:

                cursor.execute(
                    """
                    INSERT INTO ejercicios (
                        empresa_id,
                        anio,
                        fecha_apertura,
                        fecha_cierre,
                        estado
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
                        ejercicio.empresa_id,
                        ejercicio.anio,
                        ejercicio.fecha_apertura,
                        ejercicio.fecha_cierre,
                        ejercicio.estado.name,
                    ),
                )

                ejercicio.id = cursor.fetchone()[0]

            else:

                cursor.execute(
                    """
                    INSERT INTO ejercicios (
                        id,
                        empresa_id,
                        anio,
                        fecha_apertura,
                        fecha_cierre,
                        estado
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
                        anio = EXCLUDED.anio,
                        fecha_apertura = EXCLUDED.fecha_apertura,
                        fecha_cierre = EXCLUDED.fecha_cierre,
                        estado = EXCLUDED.estado
                    """,
                    (
                        ejercicio.id,
                        ejercicio.empresa_id,
                        ejercicio.anio,
                        ejercicio.fecha_apertura,
                        ejercicio.fecha_cierre,
                        ejercicio.estado.name,
                    ),
                )

        self._connection.commit()

    # =========================================================
    # LISTAR
    # =========================================================

    def listar(
        self,
    ) -> list[Ejercicio]:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    id,
                    empresa_id,
                    anio,
                    fecha_apertura,
                    fecha_cierre,
                    estado
                FROM ejercicios
                ORDER BY empresa_id, anio
                """
            )

            filas = cursor.fetchall()

        return [
            self._fila_a_ejercicio(
                fila,
            )
            for fila in filas
        ]

    # =========================================================
    # BUSCAR POR ID
    # =========================================================

    def buscar_por_id(
        self,
        ejercicio_id: int,
    ) -> Ejercicio | None:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    id,
                    empresa_id,
                    anio,
                    fecha_apertura,
                    fecha_cierre,
                    estado
                FROM ejercicios
                WHERE id = %s
                """,
                (
                    ejercicio_id,
                ),
            )

            fila = cursor.fetchone()

        if fila is None:
            return None

        return self._fila_a_ejercicio(
            fila,
        )

    # =========================================================
    # BUSCAR POR AÑO
    # =========================================================

    def buscar_por_anio(
        self,
        empresa_id: int,
        anio: int,
    ) -> Ejercicio | None:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    id,
                    empresa_id,
                    anio,
                    fecha_apertura,
                    fecha_cierre,
                    estado
                FROM ejercicios
                WHERE empresa_id = %s
                  AND anio = %s
                """,
                (
                    empresa_id,
                    anio,
                ),
            )

            fila = cursor.fetchone()

        if fila is None:
            return None

        return self._fila_a_ejercicio(
            fila,
        )

    # =========================================================
    # BUSCAR ABIERTO
    # =========================================================

    def buscar_abierto(
        self,
        empresa_id: int,
    ) -> Ejercicio | None:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    id,
                    empresa_id,
                    anio,
                    fecha_apertura,
                    fecha_cierre,
                    estado
                FROM ejercicios
                WHERE empresa_id = %s
                  AND estado = %s
                ORDER BY anio DESC
                LIMIT 1
                """,
                (
                    empresa_id,
                    EstadoEjercicio.ABIERTO.name,
                ),
            )

            fila = cursor.fetchone()

        if fila is None:
            return None

        return self._fila_a_ejercicio(
            fila,
        )

    # =========================================================
    # ELIMINAR
    # =========================================================

    def eliminar(
        self,
        id_: int,
    ) -> None:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                DELETE FROM ejercicios
                WHERE id = %s
                """,
                (
                    id_,
                ),
            )

        self._connection.commit()

    # =========================================================
    # MODIFICAR
    # =========================================================

    def modificar(
        self,
        ejercicio: Ejercicio,
    ) -> None:

        with self._connection.cursor() as cursor:

            cursor.execute(
                """
                UPDATE ejercicios
                SET
                    empresa_id = %s,
                    anio = %s,
                    fecha_apertura = %s,
                    fecha_cierre = %s,
                    estado = %s
                WHERE id = %s
                """,
                (
                    ejercicio.empresa_id,
                    ejercicio.anio,
                    ejercicio.fecha_apertura,
                    ejercicio.fecha_cierre,
                    ejercicio.estado.name,
                    ejercicio.id,
                ),
            )

        self._connection.commit()

    # =========================================================
    # MAPPER
    # =========================================================

    @staticmethod
    def _fila_a_ejercicio(
        fila,
    ) -> Ejercicio:

        return Ejercicio(

            id=fila[0],

            empresa_id=fila[1],

            anio=fila[2],

            fecha_apertura=fila[3],

            fecha_cierre=fila[4],

            estado=EstadoEjercicio[
                fila[5]
            ],
        )