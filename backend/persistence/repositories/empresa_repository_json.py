from pathlib import Path

from domain.entities.empresa import Empresa
from domain.repositories.empresa_repository import EmpresaRepository

from persistence.json_storage import JsonStorage


class EmpresaRepositoryJson(EmpresaRepository):

    def __init__(
            self,
            file_path: Path | None = None,
        ):

        if file_path is None:
            file_path = Path("data/empresas.json")

        self.storage = JsonStorage(file_path)
    # def guardar(
    #     self,
    #     empresa: Empresa,
    # ) -> None:
    #     raise NotImplementedError
    def guardar(
        self,
        empresa: Empresa,
    ) -> None:

        empresas = self.storage.read_list(
            "empresas"
        )

        empresas.append(
            self._to_dict(empresa)
        )

        self.storage.write_list(
            "empresas",
            empresas,
        )

    # def obtener_todas(
    #     self,
    # ) -> list[Empresa]:
    #     raise NotImplementedError
    def obtener_todas(
        self,
    ) -> list[Empresa]:

        datos = self.storage.read_list(
            "empresas"
        )

        return [
            self._from_dict(item)
            for item in datos
        ]

    # def buscar_por_cuit(
    #     self,
    #     cuit: str,
    # ) -> Empresa | None:
    #     raise NotImplementedError
    def buscar_por_cuit(
        self,
        cuit: str,
    ) -> Empresa | None:

        empresas = self.obtener_todas()

        for empresa in empresas:

            if empresa.cuit == cuit:
                return empresa

        return None

    # def eliminar(
    #     self,
    #     empresa: Empresa,
    # ) -> None:
    #     raise NotImplementedError
    def eliminar(
        self,
        empresa: Empresa,
    ) -> None:

        empresas = self.storage.read_list(
            "empresas"
        )

        empresas = [
            item
            for item in empresas
            if item["cuit"] != empresa.cuit
        ]

        self.storage.write_list(
            "empresas",
            empresas,
        )

        
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