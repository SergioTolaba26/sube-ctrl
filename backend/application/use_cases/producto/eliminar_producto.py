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
        empresa_id: int,
        producto_id: int,
    ) -> bool:

        producto = self._repository.buscar_por_id(
            empresa_id,
            producto_id,
        )

        if producto is None:
            return False

        return self._repository.eliminar(
            empresa_id,
            producto_id,
        )