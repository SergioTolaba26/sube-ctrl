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

    # def guardar(
    #     self,
    #     movimiento,
    # ):

    #     self.repository.guardar(
    #         movimiento,
    #     )
    # def guardar(
    #     self,
    #     movimiento,
    # ):

    #     movimientos = self.repository.listar()

    #     if not movimientos:

    #         movimiento.id = 1

    #     else:

    #         movimiento.id = max(
    #             m.id
    #             for m in movimientos
    #         ) + 1

    #     self.repository.guardar(
    #         movimiento,
    #     )
    # MODIFICACION PARA QUE AL HACER UN UPDATE no agruegue otro id
    def guardar(
        self,
        movimiento,
    ):

        if movimiento.id is None:

            movimientos = self.repository.listar()

            if not movimientos:

                movimiento.id = 1

            else:

                movimiento.id = max(
                    m.id
                    for m in movimientos
                ) + 1

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