from domain.entities.producto import Producto
from domain.repositories.producto_repository import (
    ProductoRepository,
)


class BuscarProducto:

    def __init__(
        self,
        repository: ProductoRepository,
    ):
        self._repository = repository

    def execute(
        self,
        producto_id: int,
    ) -> Producto | None:

        return self._repository.buscar_por_id(
            producto_id,
        )