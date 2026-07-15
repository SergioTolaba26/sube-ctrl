from pathlib import Path

from domain.entities.empresa import Empresa
from domain.repositories.empresa_repository import EmpresaRepository

from persistence.repositories.base_repository_json import (
    BaseRepositoryJson,
)


class EmpresaRepositoryJson(
    BaseRepositoryJson,
    EmpresaRepository,
):

    def __init__(
        self,
        file_path: Path | None = None,
    ):

        if file_path is None:
            file_path = Path(
                "data/empresas.json"
            )

        super().__init__(
            file_path,
            "empresas",
        )

    def buscar_por_cuit(
        self,
        cuit: str,
    ) -> Empresa | None:

        for empresa in self.obtener_todas():

            if empresa.cuit == cuit:
                return empresa

        return None

    def obtener_todas(
        self,
    ) -> list[Empresa]:

        return self.obtener_todos()

    def _to_dict(
        self,
        empresa: Empresa,
    ) -> dict:

        return {

            "id": empresa.id,

            "razon_social": empresa.razon_social,

            "nombre_fantasia": empresa.nombre_fantasia,

            "cuit": empresa.cuit,

            "activa": empresa.activa,

        }

    def _from_dict(
        self,
        data: dict,
    ) -> Empresa:

        return Empresa(

            id=data["id"],

            razon_social=data["razon_social"],

            nombre_fantasia=data["nombre_fantasia"],

            cuit=data["cuit"],

            activa=data["activa"],

        )