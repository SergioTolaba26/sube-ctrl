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

    def listar(
        self,
    ):

        datos = self.storage.load()

        return self.mapper.from_dict_list(
            datos,
            self.cuenta_repository,
        )