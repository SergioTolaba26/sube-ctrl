from domain.repositories.empresa_repository import (
    EmpresaRepository,
)
from domain.entities.empresa import Empresa


class RegistrarEmpresa:

    def __init__(
        self,
        repository: EmpresaRepository,
    ):

        self.repository = repository

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
        self.repository.guardar(
        empresa
        )

        return empresa