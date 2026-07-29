from datetime import date

from domain.entities.ejercicio import (
    Ejercicio,
)


class EjercicioService:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    def listar(
        self,
    ) -> list[Ejercicio]:

        return self.repository.listar()

    def buscar_por_id(
        self,
        id_,
    ):

        return self.repository.buscar_por_id(
            id_,
        )

    def buscar_por_fecha(
        self,
        fecha: date,
    ):

        for ejercicio in self.repository.listar():

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

    def guardar(
        self,
        ejercicio,
    ):

        if ejercicio.id is None:

            ejercicios = self.repository.listar()

            if not ejercicios:

                ejercicio.id = 1

            else:

                ejercicio.id = (
                    max(
                        e.id
                        for e in ejercicios
                    )
                    + 1
                )

        self.repository.guardar(
            ejercicio,
        )

    def eliminar(
        self,
        id_,
    ):

        self.repository.eliminar(
            id_,
        )
    def guardar(
        self,
        ejercicio,
    ):

        if ejercicio.id is None:

            ejercicios = self.repository.listar()

            if not ejercicios:

                ejercicio.id = 1

            else:

                ejercicio.id = max(
                    e.id
                    for e in ejercicios
                ) + 1

        self.repository.guardar(
            ejercicio,
        )

    def buscar_por_anio(
        self,
        anio: int,
    ):

        return self.repository.buscar_por_anio(
            anio,
        )


    def buscar_abierto(
        self,
    ):

        return self.repository.buscar_abierto()