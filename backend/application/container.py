from infrastructure.postgres.database import (
    DatabasePostgres,
)

from infrastructure.postgres.producto_repository import (
    ProductoRepositoryPostgres,
)

from application.use_cases.producto.registrar_producto import (
    RegistrarProducto,
)

from application.use_cases.producto.listar_productos import (
    ListarProductos,
)

from application.use_cases.producto.buscar_producto import (
    BuscarProducto,
)

from application.use_cases.producto.buscar_producto_por_codigo_barras import (
    BuscarProductoPorCodigoBarras,
)

from application.use_cases.producto.modificar_producto import (
    ModificarProducto,
)

from application.use_cases.producto.eliminar_producto import (
    EliminarProducto,
)


class ApplicationContainer:

    def __init__(self):

        # -------------------------
        # Infraestructura
        # -------------------------

        self.database = DatabasePostgres()

        self.producto_repository = (
            ProductoRepositoryPostgres(
                self.database.connection,
            )
        )

        # -------------------------
        # Casos de uso
        # -------------------------

        self._registrar_producto = None
        self._listar_productos = None
        self._buscar_producto = None
        self._buscar_producto_por_codigo_barras = None
        self._modificar_producto = None
        self._eliminar_producto = None

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
                )
            )

        return self._listar_productos

    def buscar_producto(self):

        if self._buscar_producto is None:

            self._buscar_producto = (
                BuscarProducto(
                    self.producto_repository,
                )
            )

        return self._buscar_producto

    def buscar_producto_por_codigo_barras(self):

        if (
            self._buscar_producto_por_codigo_barras
            is None
        ):

            self._buscar_producto_por_codigo_barras = (
                BuscarProductoPorCodigoBarras(
                    self.producto_repository,
                )
            )

        return (
            self._buscar_producto_por_codigo_barras
        )

    def modificar_producto(self):

        if self._modificar_producto is None:

            self._modificar_producto = (
                ModificarProducto(
                    self.producto_repository,
                )
            )

        return self._modificar_producto

    def eliminar_producto(self):

        if self._eliminar_producto is None:

            self._eliminar_producto = (
                EliminarProducto(
                    self.producto_repository,
                )
            )

        return self._eliminar_producto