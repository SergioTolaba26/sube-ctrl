from pathlib import Path

from persistence.json_storage import JsonStorage

from infrastructure.repositories.json.cuenta_repository import (
    CuentaRepositoryJson,
)

from infrastructure.repositories.json.movimiento_repository import (
    MovimientoRepositoryJson,
)

from domain.services.cuenta_service import (
    CuentaService,
)

from domain.services.movimiento_service import (
    MovimientoService,
)

from application.use_cases.cuenta.registrar_cuenta import (
    RegistrarCuenta,
)

from application.use_cases.movimiento.registrar_movimiento import (
    RegistrarMovimiento,
)

from application.use_cases.movimiento.buscar_movimiento import (
    BuscarMovimiento,
)

from application.use_cases.movimiento.listar_movimientos import (
    ListarMovimientos,
)

from application.use_cases.movimiento.modificar_movimiento import (
    ModificarMovimiento,
)

from application.use_cases.movimiento.eliminar_movimiento import (
    EliminarMovimiento,
)

from application.use_cases.movimiento.confirmar_movimiento import (
    ConfirmarMovimiento,
)

from application.use_cases.movimiento.agregar_linea_movimiento import (
    AgregarLineaMovimiento,
)

from application.use_cases.movimiento.modificar_linea_movimiento import (
    ModificarLineaMovimiento,
)

from application.use_cases.movimiento.eliminar_linea_movimiento import (
    EliminarLineaMovimiento,
)

from application.use_cases.cuenta.buscar_cuenta_por_codigo import (
    BuscarCuentaPorCodigo,
)
class ApplicationFactory:

    def __init__(self):

        self.cuenta_storage = JsonStorage(
            Path("data/cuentas.json"),
        )

        self.movimiento_storage = JsonStorage(
            Path("data/movimientos.json"),
        )

        self.cuenta_repository = CuentaRepositoryJson(
            self.cuenta_storage,
        )

        self.movimiento_repository = MovimientoRepositoryJson(
            self.movimiento_storage,
            self.cuenta_repository,
        )

        self.cuenta_service = CuentaService(
            self.cuenta_repository,
        )

        self.movimiento_service = MovimientoService(
            self.movimiento_repository,
        )

    # ---------------- CUENTAS ----------------

    def registrar_cuenta(self):

        return RegistrarCuenta(
            self.cuenta_service,
        )
    def buscar_cuenta_por_codigo(
        self,
    ):

        return BuscarCuentaPorCodigo(
            self.cuenta_service,
        )
    # --------------- MOVIMIENTOS -------------

    def registrar_movimiento(self):

        return RegistrarMovimiento(
            self.movimiento_service,
        )

    def buscar_movimiento(self):

        return BuscarMovimiento(
            self.movimiento_service,
        )

    def listar_movimientos(self):

        return ListarMovimientos(
            self.movimiento_service,
        )

    def modificar_movimiento(self):

        return ModificarMovimiento(
            self.movimiento_service,
        )

    def eliminar_movimiento(self):

        return EliminarMovimiento(
            self.movimiento_service,
        )

    def confirmar_movimiento(self):

        return ConfirmarMovimiento(
            self.movimiento_service,
        )

    def agregar_linea_movimiento(self):

        return AgregarLineaMovimiento(
            self.movimiento_service,
            self.cuenta_service,
        )

    def modificar_linea_movimiento(self):

        return ModificarLineaMovimiento(
            self.movimiento_service,
            self.cuenta_service,    
        )

    def eliminar_linea_movimiento(self):

        return EliminarLineaMovimiento(
            self.movimiento_service,
        )