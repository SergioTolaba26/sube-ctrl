from infrastructure.repositories.json.base_repository import (
    BaseRepositoryJson,
)

from infrastructure.mappers.ejercicio_contable_mapper import (
    EjercicioContableMapper,
)

class EjercicioContableRepositoryJson(
    BaseRepositoryJson,
):

    def __init__(
        self,
        storage,
    ):
        super().__init__(
            storage=storage,
            mapper=EjercicioContableMapper,
        )

    def obtener_abierto(
        self,
    ):

        for ejercicio in self.listar():

            if ejercicio.esta_abierto():

                return ejercicio

        return None