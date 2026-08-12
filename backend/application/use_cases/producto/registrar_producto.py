from domain.entities.producto import Producto
from domain.errors.producto_duplicado_error import (
    ProductoDuplicadoError,
)
from domain.repositories.producto_repository import (
    ProductoRepository,
)


class RegistrarProducto:

    def __init__(
        self,
        repository: ProductoRepository,
    ):
        self._repository = repository

    def execute(
        self,
        empresa_id: int,
        producto: Producto,
    ) -> Producto:

        producto.empresa_id = empresa_id

        existente = self._repository.buscar_por_codigo_barras(
            empresa_id,
            producto.codigo_barras,
        )

        if existente is not None:
            raise ProductoDuplicadoError(
                producto.codigo_barras,
            )

        return self._repository.guardar(
            producto,
        )