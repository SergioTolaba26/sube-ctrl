from domain.entities.producto import Producto
from domain.repositories.producto_repository import (
    ProductoRepository,
)


class ModificarProducto:

    def __init__(
        self,
        repository: ProductoRepository,
    ):
        self._repository = repository

    def execute(
        self,
        producto: Producto,
    ) -> Producto:

        return self._repository.actualizar(
            producto,
        )