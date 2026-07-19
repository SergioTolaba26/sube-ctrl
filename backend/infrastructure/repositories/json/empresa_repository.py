from infrastructure.repositories.json.base_repository import (
    BaseRepositoryJson,
)

from infrastructure.mappers.empresa_mapper import (
    EmpresaMapper,
)


class EmpresaRepositoryJson(
    BaseRepositoryJson,
):

    def __init__(
        self,
        storage,
    ):

        super().__init__(
            storage,
            EmpresaMapper,
        )

    def buscar_por_cuit(
        self,
        cuit,
    ):

        for empresa in self.listar():

            if empresa.cuit == cuit:
                return empresa

        return None
        