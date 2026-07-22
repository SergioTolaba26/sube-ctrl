from domain.repositories.empresa_repository import (
    EmpresaRepository,
)
# from domain.services.empresa_service import (
#     EmpresaService,
# )

class ListarEmpresas:

    # def __init__(
    #     self,
    #     repository: EmpresaRepository,
    # ):
    #     self.repository = repository

    def __init__(
        self,
        repository: EmpresaRepository,
    ):
        self.repository = repository

    def execute(
        self,
    ):
        return self.repository.obtener_todas()
        # Dimos marcha atras
        #return self.service.listar()