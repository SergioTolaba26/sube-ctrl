from domain.entities.producto import Producto
from domain.repositories.producto_repository import (
    ProductoRepository,
)


class BuscarProductoPorCodigoBarras:

    def __init__(
        self,
        repository: ProductoRepository,
    ):
        self._repository = repository

    def execute(
        self,
        empresa_id: int,
        codigo_barras: str,
    ) -> Producto | None:

        return self._repository.buscar_por_codigo_barras(
            empresa_id,
            codigo_barras,
        )