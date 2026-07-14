from domain.entities.empresa import Empresa

from domain.errors.empresa_duplicada_error import (
    EmpresaDuplicadaError,
)

class RegistrarEmpresa:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    def ejecutar(
        self,
        razon_social: str,
        nombre_fantasia: str,
        cuit: str,
    ) -> Empresa:

        empresa_existente = (
            self.repository.buscar_por_cuit(
                cuit
            )
        )

        if empresa_existente is not None:
           raise EmpresaDuplicadaError(
            "Ya existe una empresa con ese CUIT."
        )   

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