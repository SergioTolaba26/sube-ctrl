from domain.entities.ejercicio_contable import (
    EjercicioContable,
)
from datetime import date

from domain.entities.ejercicio_contable import (
    EjercicioContable,
)
from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)


class EjercicioContableService:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    def listar(
        self,
    ) -> list[EjercicioContable]:

        return self.repository.listar()

    def buscar_por_id(
        self,
        id_,
    ):

        return self.repository.buscar_por_id(
            id_,
        )

    def obtener_abierto(
        self,
    ):

        return self.repository.obtener_abierto()

    def guardar(
        self,
        ejercicio,
    ):

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



