# from domain.repositories.empresa_repository import (
#     EmpresaRepository,
# )
from domain.entities.empresa import Empresa
from domain.services.empresa_service import (
    EmpresaService,
)

class RegistrarEmpresa:

    def __init__(
        self,
        service: EmpresaService,
    ):
        self.service = service

# class RegistrarEmpresa:

#     def __init__(
#         self,
#         repository: EmpresaRepository,
#     ):

#         self.repository = repository

    # def execute(
    #     self,
    #     razon_social: str,
    #     nombre_fantasia: str,
    #     cuit: str,
    # ):
    #     pass

    def execute(
        self,
        razon_social: str,
        nombre_fantasia: str,
        cuit: str,
        ):

        empresa = Empresa(
            id=None,
            razon_social=razon_social,
            nombre_fantasia=nombre_fantasia,
            cuit=cuit,
        )
        # self.repository.guardar(
        # empresa
        # )
        self.service.guardar(
        empresa,
        )

        return empresa