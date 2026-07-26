from infrastructure.persistence.base.storage import (
    Storage,
)

from infrastructure.mappers.cuenta_mapper import (
    CuentaMapper,
)

#class CuentaRepositoryJson:
from infrastructure.repositories.json.base_repository import (
    BaseRepositoryJson,
)

class CuentaRepositoryJson(
    BaseRepositoryJson,
):
    def __init__(
        self,
        storage: Storage,
    ):
        super().__init__(
            storage=storage,
            mapper=CuentaMapper,
        )

    def buscar_por_codigo(
        self,
        codigo: str,
    ):

        for cuenta in self.listar():

            if cuenta.codigo == codigo:
                return cuenta

        return None
    
   