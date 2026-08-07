from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)


class MovimientoRepositoryStub(
    MovimientoRepository,
):

    def __init__(self):

        self.movimientos = []

    def listar(
        self,
    ):
        return self.movimientos

    def guardar(
        self,
        movimiento,
    ):

        existente = self.buscar_por_id(
            movimiento.id,
        )

        if existente is None:

            self.movimientos.append(
                movimiento,
            )

        else:

            indice = self.movimientos.index(
                existente,
            )

            self.movimientos[indice] = (
                movimiento
            )

    def obtener_todos(self):
        return self.movimientos



    def eliminar(
        self,
        movimiento_id,
    ):

        movimiento = self.buscar_por_id(
            movimiento_id,
        )

        if movimiento is not None:

            self.movimientos.remove(
                movimiento,
            )

    def buscar_por_id(
        self,
        id,
    ):
        for movimiento in self.movimientos:
            if movimiento.id == id:
                return movimiento

        return None

    def listar_por_fecha(
        self,
        desde,
        hasta,
    ):

        movimientos = self.listar()

        if desde is not None:

            movimientos = [
                movimiento
                for movimiento in movimientos
                if movimiento.fecha >= desde
            ]

        if hasta is not None:

            movimientos = [
                movimiento
                for movimiento in movimientos
                if movimiento.fecha <= hasta
            ]

        return movimientos
