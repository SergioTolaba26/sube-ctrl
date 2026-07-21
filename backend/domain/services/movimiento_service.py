from domain.entities.movimiento import (
    Movimiento,
)


class MovimientoService:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    def listar(
        self,
    ) -> list[Movimiento]:

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
        movimiento,
    ):

        self.repository.guardar(
            movimiento,
        )

    def eliminar(
        self,
        id_,
    ):

        self.repository.eliminar(
            id_,
        )