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
        empresa_context,
    ):

        self._repository = repository
        self._empresa_context = empresa_context

    def execute(
        self,
        producto: Producto,
    ) -> Producto:

        empresa_id = (
            self._empresa_context.obtener_empresa_id()
        )

        producto.empresa_id = empresa_id

        existente = (
            self._repository.buscar_por_codigo_barras(
                empresa_id,
                producto.codigo_barras,
            )
        )

        if existente is not None:
            raise ProductoDuplicadoError()

        return self._repository.guardar(
            producto,
        )