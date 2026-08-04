from domain.entities.producto import Producto
from domain.errors.producto_duplicado_error import (
    ProductoDuplicadoError,
)
from domain.repositories.producto_repository import (
    ProductoRepository,
)


class CrearProducto:

    def __init__(
        self,
        repository: ProductoRepository,
    ):
        self._repository = repository

    def execute(
        self,
        producto: Producto,
    ) -> Producto:

        existente = (
            self._repository.buscar_por_codigo_barras(
                producto.codigo_barras,
            )
        )

        if existente is not None:
            raise ProductoDuplicadoError(
                "Ya existe un producto con ese código de barras."
            )

        return self._repository.guardar(
            producto,
        )