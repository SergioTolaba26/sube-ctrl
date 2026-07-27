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