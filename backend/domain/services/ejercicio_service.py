from datetime import date

from domain.entities.ejercicio import Ejercicio


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
        ejercicio_id: int,
    ):

        return self.repository.buscar_por_id(
            ejercicio_id,
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
        ejercicio: Ejercicio,
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
        id_: int,
    ):

        self.repository.eliminar(
            id_,
        )

    def modificar(
        self,
        ejercicio: Ejercicio,
    ):

        self.repository.modificar(
            ejercicio,
        )

        return ejercicio

    def buscar_por_anio(
        self,
        empresa_id: int,
        anio: int,
    ):

        return self.repository.buscar_por_anio(
            empresa_id,
            anio,
        )

    def buscar_abierto(
        self,
        empresa_id: int,
    ):

        return self.repository.buscar_abierto(
            empresa_id,
        )