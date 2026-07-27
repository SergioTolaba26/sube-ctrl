from infrastructure.persistence.base.storage import (
    Storage,
)

from infrastructure.repositories.json.base_repository import (
    BaseRepositoryJson,
)

from infrastructure.mappers.ejercicio_mapper import (
    EjercicioMapper,
)


class EjercicioRepositoryJson(
    BaseRepositoryJson,
):

    def __init__(
        self,
        storage: Storage,
    ):
        super().__init__(
            storage=storage,
            mapper=EjercicioMapper,
        )

    def buscar_por_anio(
        self,
        anio: int,
    ):

        for ejercicio in self.listar():

            if ejercicio.anio == anio:
                return ejercicio

        return None