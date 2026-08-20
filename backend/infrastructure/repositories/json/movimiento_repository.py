from infrastructure.mappers.movimiento_mapper import (
    MovimientoMapper,
)

from infrastructure.repositories.json.base_repository import (
    BaseRepositoryJson,
)


class MovimientoRepositoryJson(
    BaseRepositoryJson,
):

    def __init__(
        self,
        storage,
        cuenta_repository,
    ):
        self.cuenta_repository = (
            cuenta_repository
        )

        super().__init__(
            storage=storage,
            mapper=MovimientoMapper,
        )
    def _listar_todas(
        self,
    ):

        datos = self.storage.load()

        return self.mapper.from_dict_list(
            datos,
            self.cuenta_repository,
        )
    def listar(
        self,
    ):

        datos = self.storage.load()

        return self.mapper.from_dict_list(
            datos,
            self.cuenta_repository,
        )
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

    def buscar_por_id(
        self,
        id_,
    ):

        for movimiento in self.listar():

            if movimiento.id == id_:
                return movimiento

        return None