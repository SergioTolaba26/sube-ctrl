from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)


class EjercicioRepositoryStub:

    def __init__(self):
        self.ejercicios = []

    # =========================================================
    # GUARDAR
    # =========================================================

    def guardar(
        self,
        ejercicio,
    ):

        # Simula el comportamiento de PostgreSQL:
        # si no tiene ID, genera uno.
        if ejercicio.id is None:

            if self.ejercicios:

                ejercicio.id = max(
                    e.id
                    for e in self.ejercicios
                    if e.id is not None
                ) + 1

            else:

                ejercicio.id = 1

        self.ejercicios.append(
            ejercicio,
        )

    # =========================================================
    # BUSCAR POR ID
    #
    # Compatible con:
    #
    # buscar_por_id(id)
    #
    # y:
    #
    # buscar_por_id(empresa_id, id)
    # =========================================================

    def buscar_por_id(
        self,
        empresa_id_o_id: int | None = None,
        ejercicio_id: int | None = None,
        *,
        empresa_id: int | None = None,
    ):

        # Permite:
        #
        # buscar_por_id(1)
        #
        # buscar_por_id(empresa_id, ejercicio_id)
        #
        # buscar_por_id(
        #     empresa_id=1,
        #     ejercicio_id=2,
        # )

        if empresa_id is not None:

            empresa_id_o_id = empresa_id

        if ejercicio_id is None:

            ejercicio_id = empresa_id_o_id

            for ejercicio in self.ejercicios:

                if ejercicio.id == ejercicio_id:

                    return ejercicio

            return None

        empresa_id = empresa_id_o_id

        for ejercicio in self.ejercicios:

            if (
                ejercicio.id == ejercicio_id
                and ejercicio.empresa_id == empresa_id
            ):

                return ejercicio

        return None

    # =========================================================
    # LISTAR
    #
    # Compatible con:
    #
    # listar()
    #
    # y:
    #
    # listar(empresa_id)
    # =========================================================

    def listar(
        self,
        empresa_id: int | None = None,
    ):

        if empresa_id is None:

            return list(
                self.ejercicios,
            )

        return [
            ejercicio
            for ejercicio in self.ejercicios
            if ejercicio.empresa_id == empresa_id
        ]

    # =========================================================
    # BUSCAR POR AÑO
    # =========================================================

    def buscar_por_anio(
        self,
        empresa_id: int,
        anio: int,
    ):

        for ejercicio in self.ejercicios:

            if (
                ejercicio.empresa_id == empresa_id
                and ejercicio.anio == anio
            ):

                return ejercicio

        return None

    # =========================================================
    # BUSCAR ABIERTO
    # =========================================================

    def buscar_abierto(
        self,
        empresa_id: int,
    ):

        for ejercicio in self.ejercicios:

            if (
                ejercicio.empresa_id == empresa_id
                and ejercicio.estado
                == EstadoEjercicio.ABIERTO
            ):

                return ejercicio

        return None

    # =========================================================
    # ELIMINAR
    #
    # Compatible con:
    #
    # eliminar(id)
    #
    # y:
    #
    # eliminar(empresa_id, id)
    # =========================================================

    def eliminar(
        self,
        empresa_id_o_id: int,
        ejercicio_id: int | None = None,
    ):

        if ejercicio_id is None:

            ejercicio_id = empresa_id_o_id

            self.ejercicios = [
                ejercicio
                for ejercicio in self.ejercicios
                if ejercicio.id != ejercicio_id
            ]

            return

        empresa_id = empresa_id_o_id

        self.ejercicios = [
            ejercicio
            for ejercicio in self.ejercicios
            if not (
                ejercicio.id == ejercicio_id
                and ejercicio.empresa_id == empresa_id
            )
        ]

    # =========================================================
    # MODIFICAR
    # =========================================================

    def modificar(
        self,
        ejercicio,
    ):

        for indice, existente in enumerate(
            self.ejercicios
        ):

            if (
                existente.id == ejercicio.id
                and existente.empresa_id
                == ejercicio.empresa_id
            ):

                self.ejercicios[indice] = ejercicio

                return

        # Si no encuentra por empresa + ID, no hace nada.