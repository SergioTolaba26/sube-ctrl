from domain.entities.empresa import Empresa


class BuscarEmpresa:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    def ejecutar(
        self,
        cuit: str,
    ) -> Empresa | None:

        return self.repository.buscar_por_cuit(
            cuit
        )