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

    # def guardar(
    #     self,
    #     empresa,
    # ):

    #     self.repository.guardar(
    #         empresa,
    #     )

    def guardar(
        self,
        empresa,
    ):

        empresas = self.repository.listar()

        if len(empresas) == 0:

            nuevo_id = 1

        else:

            nuevo_id = max(
                e.id
                for e in empresas
            ) + 1

        empresa.id = nuevo_id

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