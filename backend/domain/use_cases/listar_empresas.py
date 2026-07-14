from domain.entities.empresa import Empresa


class ListarEmpresas:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    def ejecutar(
        self,
    ) -> list[Empresa]:

        return self.repository.obtener_todas()