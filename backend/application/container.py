from infrastructure.postgres.database import (
    DatabasePostgres,
)

# =========================================================
# REPOSITORIOS
# =========================================================

from infrastructure.postgres.producto_repository import (
    ProductoRepositoryPostgres,
)

from infrastructure.postgres.cuenta_repository import (
    CuentaRepositoryPostgres,
)

# =========================================================
# CASOS DE USO - PRODUCTOS
# =========================================================

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

# =========================================================
# CASOS DE USO - CUENTAS
# =========================================================

from application.use_cases.cuenta.registrar_cuenta import (
    RegistrarCuenta,
)

from application.use_cases.cuenta.listar_cuentas import (
    ListarCuentas,
)

from application.use_cases.cuenta.buscar_cuenta import (
    BuscarCuenta,
)

from application.use_cases.cuenta.buscar_cuenta_por_codigo import (
    BuscarCuentaPorCodigo,
)

from application.use_cases.cuenta.modificar_cuenta import (
    ModificarCuenta,
)

from application.use_cases.cuenta.eliminar_cuenta import (
    EliminarCuenta,
)


class ApplicationContainer:

    def __init__(self):

        # =================================================
        # INFRAESTRUCTURA
        # =================================================

        self.database = DatabasePostgres()

        # -------------------------------------------------
        # REPOSITORIO PRODUCTOS
        # -------------------------------------------------

        self.producto_repository = (
            ProductoRepositoryPostgres(
                self.database.connection,
            )
        )

        # -------------------------------------------------
        # REPOSITORIO CUENTAS
        # -------------------------------------------------

        self.cuenta_repository = (
            CuentaRepositoryPostgres(
                self.database.connection,
            )
        )

        # =================================================
        # CASOS DE USO - PRODUCTOS
        # =================================================

        self._registrar_producto = None
        self._listar_productos = None
        self._buscar_producto = None
        self._buscar_producto_por_codigo_barras = None
        self._modificar_producto = None
        self._eliminar_producto = None

        # =================================================
        # CASOS DE USO - CUENTAS
        # =================================================

        self._registrar_cuenta = None
        self._listar_cuentas = None
        self._buscar_cuenta = None
        self._buscar_cuenta_por_codigo = None
        self._modificar_cuenta = None
        self._eliminar_cuenta = None

    # =====================================================
    # PRODUCTOS
    # =====================================================

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

    # =====================================================
    # CUENTAS
    # =====================================================

    def registrar_cuenta(self):

        if self._registrar_cuenta is None:

            self._registrar_cuenta = (
                RegistrarCuenta(
                    self.cuenta_repository,
                )
            )

        return self._registrar_cuenta

    def listar_cuentas(self):

        if self._listar_cuentas is None:

            self._listar_cuentas = (
                ListarCuentas(
                    self.cuenta_repository,
                )
            )

        return self._listar_cuentas

    def buscar_cuenta(self):

        if self._buscar_cuenta is None:

            self._buscar_cuenta = (
                BuscarCuenta(
                    self.cuenta_repository,
                )
            )

        return self._buscar_cuenta

    def buscar_cuenta_por_codigo(self):

        if self._buscar_cuenta_por_codigo is None:

            self._buscar_cuenta_por_codigo = (
                BuscarCuentaPorCodigo(
                    self.cuenta_repository,
                )
            )

        return self._buscar_cuenta_por_codigo

    def modificar_cuenta(self):

        if self._modificar_cuenta is None:

            self._modificar_cuenta = (
                ModificarCuenta(
                    self.cuenta_repository,
                )
            )

        return self._modificar_cuenta

    def eliminar_cuenta(self):

        if self._eliminar_cuenta is None:

            self._eliminar_cuenta = (
                EliminarCuenta(
                    self.cuenta_repository,
                )
            )

        return self._eliminar_cuenta