from domain.repositories.empresa_repository import (
    EmpresaRepository,
)


class ModificarEmpresa:

    def __init__(
        self,
        repository: EmpresaRepository,
    ):
        self.repository = repository

    def execute(
        self,
        empresa_id: int,
        razon_social: str,
        nombre_fantasia: str,
        cuit: str,
    ):

        empresa = self.repository.buscar_por_id(
            empresa_id,
        )

        if empresa is None:
            return None

        empresa.razon_social = razon_social
        empresa.nombre_fantasia = nombre_fantasia
        empresa.cuit = cuit

        self.repository.guardar(
            empresa,
        )

        return empresa