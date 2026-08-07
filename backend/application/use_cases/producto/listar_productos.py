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
    ):
        return self._repository.obtener_todos()