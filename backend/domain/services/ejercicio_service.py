from datetime import date

from domain.entities.ejercicio import Ejercicio


class EjercicioService:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    # =========================================================
    # LISTAR
    # =========================================================

    def listar(
        self,
        empresa_id: int | None = None,
    ) -> list[Ejercicio]:

        if empresa_id is None:
            return self.repository.listar()

        return self.repository.listar(
            empresa_id,
        )

    # =========================================================
    # BUSCAR POR ID
    # =========================================================

    def buscar_por_id(
        self,
        empresa_id_o_id: int,
        ejercicio_id: int | None = None,
    ) -> Ejercicio | None:

        if ejercicio_id is None:

            return self.repository.buscar_por_id(
                empresa_id_o_id,
            )

        return self.repository.buscar_por_id(
            empresa_id_o_id,
            ejercicio_id,
        )
    # =========================================================
    # BUSCAR POR FECHA
    # =========================================================

    def buscar_por_fecha(
        self,
        empresa_id_o_fecha,
        fecha: date | None = None,
    ) -> Ejercicio | None:

        if fecha is None:

            empresa_id = 1
            fecha = empresa_id_o_fecha

        else:

            empresa_id = empresa_id_o_fecha

        for ejercicio in self.repository.listar(
            empresa_id,
        ):

            if (
                ejercicio.fecha_apertura <= fecha
                and
                (
                    ejercicio.fecha_cierre is None
                    or fecha <= ejercicio.fecha_cierre
                )
            ):

                return ejercicio

        return None
    # =========================================================
    # GUARDAR
    #
    # PostgreSQL genera el ID cuando ejercicio.id es None.
    # =========================================================

    def guardar(
        self,
        ejercicio: Ejercicio,
    ) -> None:

        self.repository.guardar(
            ejercicio,
        )

    # =========================================================
    # ELIMINAR
    # =========================================================

    def eliminar(
        self,
        empresa_id_o_id: int,
        ejercicio_id: int | None = None,
    ) -> None:

        if ejercicio_id is None:

            self.repository.eliminar(
                empresa_id_o_id,
            )

            return

        self.repository.eliminar(
            empresa_id_o_id,
            ejercicio_id,
        )
    # =========================================================
    # MODIFICAR
    # =========================================================

    def modificar(
        self,
        ejercicio: Ejercicio,
    ) -> Ejercicio:

        self.repository.modificar(
            ejercicio,
        )

        return ejercicio

    # =========================================================
    # BUSCAR POR AÑO
    # =========================================================

    def buscar_por_anio(
        self,
        empresa_id: int,
        anio: int,
    ) -> Ejercicio | None:

        return self.repository.buscar_por_anio(
            empresa_id,
            anio,
        )

    # =========================================================
    # BUSCAR ABIERTO
    # =========================================================

    def buscar_abierto(
        self,
        empresa_id: int,
    ) -> Ejercicio | None:

        return self.repository.buscar_abierto(
            empresa_id,
        )