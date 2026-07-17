from domain.entities.empresa import Empresa
from domain.repositories.empresa_repository import EmpresaRepository


class EmpresaRepositoryStub(EmpresaRepository):

    def __init__(self):

        self.empresas = []

    def guardar(
        self,
        empresa: Empresa,
    ) -> None:

        self.empresas.append(
            empresa
        )

    def obtener_todas(self):

        return self.empresas

    def buscar_por_cuit(
        self,
        cuit: str,
    ):

        for empresa in self.empresas:

            if empresa.cuit == cuit:
                return empresa

        return None

    def eliminar(
        self,
        empresa: Empresa,
    ) -> None:

        self.empresas.remove(
            empresa
        )