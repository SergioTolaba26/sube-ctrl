from application.use_cases.ejercicio.buscar_ejercicio_use_case import BuscarEjercicio
from infrastructure.repositories.json.ejercicio_repository import (
    EjercicioRepositoryJson,
)

from domain.services.ejercicio_service import (
    EjercicioService,
)

from application.use_cases.ejercicio.abrir_ejercicio import (
    AbrirEjercicio,
)
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
from application.use_cases.movimiento.registrar_asiento_contable import (
    RegistrarAsientoContable,
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

from application.use_cases.libro_diario.listar_libro_diario import (
    ListarLibroDiario,
)
from application.use_cases.libro_mayor.listar_libro_mayor import (
    ListarLibroMayor,
)
from application.use_cases.balance_sumas_saldos.listar_balance_sumas_saldos import (
    ListarBalanceSumasSaldos,
)
from application.use_cases.balance_general.listar_balance_general import (
    ListarBalanceGeneral,
)
from application.use_cases.estado_resultados.listar_estado_resultados import (
    ListarEstadoResultados,
)
from application.use_cases.balance_general.listar_balance_general import (
    ListarBalanceGeneral,
)
from application.use_cases.ejercicio.registrar_ejercicio import (
    RegistrarEjercicio,
)
class ApplicationFactory:

    def __init__(self):

        self.cuenta_storage = JsonStorage(
            Path("data/cuentas.json"),
        )

        self.movimiento_storage = JsonStorage(
            Path("data/movimientos.json"),
        )
        self.ejercicio_storage = JsonStorage(
            Path("data/ejercicios.json"),
        )   
        self.cuenta_repository = CuentaRepositoryJson(
            self.cuenta_storage,
        )

        self.movimiento_repository = MovimientoRepositoryJson(
            self.movimiento_storage,
            self.cuenta_repository,
        )
        self.ejercicio_repository = EjercicioRepositoryJson(
            self.ejercicio_storage,
        )
        self.cuenta_service = CuentaService(
            self.cuenta_repository,
        )

        self.movimiento_service = MovimientoService(
            self.movimiento_repository,
        )
        self.ejercicio_service = EjercicioService(
            self.ejercicio_repository,
        )
    ## -----iNICIO CASOS DE USO -----
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
            self.ejercicio_service,
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
            self.cuenta_service,
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
    # -----------EJERCICIOS -----------------
    def abrir_ejercicio(self):

        return AbrirEjercicio(
            self.ejercicio_service,
        )
    def buscar_ejercicio(
        self,
    ):

        return BuscarEjercicio(
            self.ejercicio_repository,
        )
    
    def registrar_ejercicio(
        self,
    ):

        return RegistrarEjercicio(
            self.ejercicio_service,
        )
    
    def registrar_asiento_contable(
        self,
    ):

        return RegistrarAsientoContable(
            self.movimiento_service,
            self.cuenta_service,
            self.ejercicio_service,
        )

    ## -----FIN CASOS DE USO ------
    # --------------REPORTES CONTABLES ----------------------
    def listar_libro_diario(
        self,
    ):

        return ListarLibroDiario(
            self.movimiento_service,
        )
    
    def listar_libro_mayor(
        self,
    ):

        return ListarLibroMayor(
            self.movimiento_service,
        )
    
    def listar_balance_sumas_saldos(
        self,
    ):

        return ListarBalanceSumasSaldos(
            self.movimiento_service,
        )
    
    def listar_balance_general(self):

        return ListarBalanceGeneral(
            self.movimiento_service,
            self.cuenta_service,
        )
        
    def listar_estado_resultados(
        self,
    ):

        return ListarEstadoResultados(
            self.movimiento_service,
            self.cuenta_service,
        )