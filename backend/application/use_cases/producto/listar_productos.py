from domain.entities.producto import Producto

from domain.repositories.producto_repository import (
    ProductoRepository,
)


class ListarProductos:

    def __init__(
        self,
        repository: ProductoRepository,
    ):
        self._repository = repository

    def execute(
        self,
        empresa_id: int,
    ) -> list[Producto]:

        return self._repository.obtener_todos(
            empresa_id,
        )