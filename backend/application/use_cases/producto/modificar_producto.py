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
        empresa_id: int,
        producto: Producto,
    ) -> Producto | None:

        producto.empresa_id = empresa_id

        existente = self._repository.buscar_por_id(
            empresa_id,
            producto.id,
        )

        if existente is None:
            return None

        return self._repository.modificar(
            producto,
        )