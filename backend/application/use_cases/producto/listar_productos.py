from domain.repositories.producto_repository import (
    ProductoRepository,
)
from application.context.empresa_context import (
    EmpresaContext,
)

class ListarProductos:

    def __init__(
        self,
        repository,
        empresa_context: EmpresaContext,
    ):
        self._repository = repository
        self._empresa_context = empresa_context

    def execute(
        self,
    ):
        empresa_id = (
            self._empresa_context.obtener_empresa_id()
        )

        return self._repository.obtener_todos(
            empresa_id,
        )