from domain.repositories.producto_repository import (
    ProductoRepository,
)


class EliminarProducto:

    def __init__(
        self,
        repository: ProductoRepository,
    ):
        self._repository = repository

    def execute(
        self,
        producto_id: int,
    ) -> None:

        self._repository.eliminar(
            producto_id,
        )