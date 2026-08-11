
from infrastructure.sqlite.database import Database
from infrastructure.sqlite.producto_repository import (
    ProductoRepositorySQLite,
)

from application.context.empresa_context import (
    EmpresaContext,
)

from application.use_cases.producto.registrar_producto import (
    RegistrarProducto,
)

from application.use_cases.producto.listar_productos import (
    ListarProductos,
)


class ApplicationContainer:

    def __init__(self):

        # -------------------------
        # Infraestructura
        # -------------------------

        self.database = Database()

        self.producto_repository = (
            ProductoRepositorySQLite(
                self.database.connection,
            )
        )

        # -------------------------
        # Contextos
        # -------------------------

        self.empresa_context = EmpresaContext()

        # -------------------------
        # Casos de uso
        # -------------------------

        self._registrar_producto = None
        self._listar_productos = None

    # -------------------------
    # PRODUCTOS
    # -------------------------

    def registrar_producto(self):

        if self._registrar_producto is None:

            self._registrar_producto = (
                RegistrarProducto(
                    self.producto_repository,
                )
            )

        return self._registrar_producto

    def listar_productos(self):

        if self._listar_productos is None:

            self._listar_productos = (
                ListarProductos(
                    self.producto_repository,
                    self.empresa_context,
                )
            )

        return self._listar_productos

