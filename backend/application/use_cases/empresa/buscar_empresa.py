# from domain.repositories.empresa_repository import (
#     EmpresaRepository,
# )
from domain.services.empresa_service import (
    EmpresaService,
)

class BuscarEmpresa:

    # def __init__(
    #     self,
    #     repository: EmpresaRepository,
    # ):
    #     self.repository = repository
    def __init__(
        self,
        service: EmpresaService,
    ):
        self.service = service
    
    def execute(
        self,
        empresa_id: int,
    ):
        # return self.repository.buscar_por_id(
        #     empresa_id
        # )
        return self.service.buscar_por_id(
            empresa_id,
        )   