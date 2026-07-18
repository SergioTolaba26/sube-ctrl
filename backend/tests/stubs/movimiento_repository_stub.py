from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)


class MovimientoRepositoryStub(
    MovimientoRepository,
):

    def __init__(self):

        self.movimientos = []

    def guardar(
        self,
        movimiento,
    ):
        self.movimientos.append(
            movimiento
        )

    def obtener_todos(self):
        return self.movimientos

    def eliminar(
        self,
        movimiento,
    ):
        self.movimientos.remove(
            movimiento
        )

    def buscar_por_id(
        self,
        id,
    ):
        for movimiento in self.movimientos:
            if movimiento.id == id:
                return movimiento

        return None