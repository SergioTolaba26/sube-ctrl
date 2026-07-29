
from datetime import date

import pytest

from application.use_cases.ejercicio.cerrar_ejercicio_use_case import (
    CerrarEjercicio,
)

from domain.enums.tipo_cuenta import TipoCuenta
from tests.factories.ejercicio_factory import (
    EjercicioFactory,
)

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)


class StubRepository:

    def __init__(
        self,
        ejercicio,
    ):
        self.ejercicio = ejercicio

    def listar(
        self,
    ):
        return [self.ejercicio]

    def buscar_por_id(
        self,
        id_,
    ):
        if self.ejercicio.id == id_:
            return self.ejercicio

        return None

    def guardar(
        self,
        ejercicio,
    ):
        self.ejercicio = ejercicio


from domain.enums.estado_movimiento import (
    EstadoMovimiento,
)


class MovimientoStub:

    def __init__(
        self,
        ejercicio_id,
        confirmado,
    ):
        self.ejercicio_id = ejercicio_id

        if confirmado:
            self.estado = EstadoMovimiento.CONFIRMADO
        else:
            self.estado = EstadoMovimiento.BORRADOR

    def esta_en_borrador(
        self,
    ):
        return (
            self.estado
            ==
            EstadoMovimiento.BORRADOR
        )

class MovimientoServiceStub:

    def __init__(
        self,
        movimientos=None,
    ):
        self._movimientos = movimientos or []
        self.movimientos_guardados = []

    def listar(
        self,
    ):
        return self._movimientos

    def guardar(
        self,
        movimiento,
    ):
        self.movimientos_guardados.append(
            movimiento,
        )
# modif test
class Cuenta:

    def __init__(
        self,
        id,
        codigo,
        nombre,
    ):
        self.id = id
        self.codigo = codigo
        self.nombre = nombre


from tests.factories.cuenta_factory import CuentaFactory


class CuentaServiceStub:

    def __init__(self):

        self.cuentas = [
            CuentaFactory.crear(
                id=9,
                codigo="4.1.01",
                nombre="Ventas",
                tipo=TipoCuenta.INGRESO,
            ),
            CuentaFactory.crear(
                id=13,
                codigo="5.3.01",
                nombre="Alquiler",
                tipo=TipoCuenta.GASTO,
            ),
            CuentaFactory.crear(
                id=8,
                codigo="3.2.01",
                nombre="Resultados Acumulados",
                tipo=TipoCuenta.PATRIMONIO,
            ),
        ]

    def listar(self):
        return self.cuentas

    def buscar_por_id(
        self,
        cuenta_id,
    ):
        for cuenta in self.cuentas:
            if cuenta.id == cuenta_id:
                return cuenta

        return None
# fin modif 
def test_cerrar_ejercicio():

    ejercicio = EjercicioFactory.crear()

    repository = StubRepository(
        ejercicio,
    )

    movimiento_service = MovimientoServiceStub()
    #modif
    cuenta_service = CuentaServiceStub()
    use_case = CerrarEjercicio(
        repository,
        movimiento_service,
        cuenta_service,
    )
    # fin modif
    resultado = use_case.execute(
        ejercicio.id,
    )

    assert resultado.estado == EstadoEjercicio.CERRADO
    assert resultado.fecha_cierre == date.today()
    # Cuando no existe resultado contable es decir Resultado = 0, no hay movimientos que guardar
    # assert len(
    #     movimiento_service.movimientos_guardados
    # ) == 1

def test_no_permite_cerrar_dos_veces():

    ejercicio = EjercicioFactory.crear(
        estado=EstadoEjercicio.CERRADO,
        fecha_cierre=date.today(),
    )

    repository = StubRepository(
        ejercicio,
    )

    movimiento_service = MovimientoServiceStub()
    #modif
    cuenta_service = CuentaServiceStub()
    use_case = CerrarEjercicio(
        repository,
        movimiento_service,
        cuenta_service,
    )
    # fin modif

    with pytest.raises(
        ValueError,
    ):
        use_case.execute(
            ejercicio.id,
        )

def test_no_permite_cerrar_con_movimientos_sin_confirmar():

    ejercicio = EjercicioFactory.crear()

    repository = StubRepository(
        ejercicio,
    )

    movimiento = MovimientoStub(
        ejercicio_id=ejercicio.id,
        confirmado=False,
    )

    movimiento_service = MovimientoServiceStub(
        movimientos=[
            movimiento,
        ],
    )

    cuenta_service = CuentaServiceStub()

    use_case = CerrarEjercicio(
        repository,
        movimiento_service,
        cuenta_service,
    )

    with pytest.raises(
        ValueError,
    ):
        use_case.execute(
            ejercicio.id,
        )

def test_cerrar_ejercicio_genera_movimiento_de_cierre():

    class EstadoResultadosStub:

        def execute(
            self,
        ):
            from decimal import Decimal

            return {
                "ingresos": [
                    {
                        "cuenta_id": 9,
                        "saldo": Decimal("1000"),
                        "debitos": Decimal("0"),
                        "creditos": Decimal("1000"),
                    }
                ],
                "egresos": [],
                "total_ingresos": Decimal("1000"),
                "total_egresos": Decimal("0"),
                "resultado": Decimal("1000"),
            }

    from application.services import cierre_contable_service

    cierre_contable_service.ListarEstadoResultados = (
        lambda *args, **kwargs: EstadoResultadosStub()
    )

    ejercicio = EjercicioFactory.crear()

    repository = StubRepository(
        ejercicio,
    )

    movimiento_service = MovimientoServiceStub()

    cuenta_service = CuentaServiceStub()

    use_case = CerrarEjercicio(
        repository,
        movimiento_service,
        cuenta_service,
    )

    resultado = use_case.execute(
        ejercicio.id,
    )

    assert resultado.estado == EstadoEjercicio.CERRADO

    assert len(
        movimiento_service.movimientos_guardados
    ) == 1