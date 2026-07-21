from domain.entities.empresa import (
    Empresa,
)


class EmpresaService:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    def listar(self) -> list[Empresa]:

        return self.repository.listar()

    def buscar_por_id(
        self,
        id_,
    ):

        return self.repository.buscar_por_id(
            id_,
        )

    def guardar(
        self,
        empresa,
    ):

        self.repository.guardar(
            empresa,
        )

    def eliminar(
        self,
        id_,
    ):

        self.repository.eliminar(
            id_,
        )