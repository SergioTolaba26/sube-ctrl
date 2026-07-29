from decimal import Decimal

from application.services.cierre_contable_service import (
    CierreContableService,
)


class MovimientoServiceStub:

    def listar(self):
        return []


class CuentaServiceStub:

    def listar(self):
        return []

    def buscar_por_id(
        self,
        cuenta_id,
    ):
        return None


def test_no_genera_asiento_si_no_hay_resultados():

    service = CierreContableService(
        MovimientoServiceStub(),
        CuentaServiceStub(),
    )

    cierre = service.calcular_cierre()

    assert cierre == []

from decimal import Decimal

from domain.enums.tipo_cuenta import TipoCuenta


class CuentaStub:

    def __init__(
        self,
        id,
        codigo,
        tipo,
    ):
        self.id = id
        self.codigo = codigo
        self.tipo = tipo


class CuentaServiceIngresoStub:

    def listar(
        self,
    ):
        return [
            CuentaStub(
                1,
                "4.1.01",
                TipoCuenta.INGRESO,
            ),
            CuentaStub(
                8,
                "3.2.01",
                TipoCuenta.PATRIMONIO,
            ),
        ]

    def buscar_por_id(
        self,
        cuenta_id,
    ):

        for cuenta in self.listar():

            if cuenta.id == cuenta_id:
                return cuenta

        return None


class EstadoResultadosIngresoStub:

    def execute(
        self,
    ):
        return {
            "ingresos": [
                {
                    "cuenta_id": 1,
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


def test_genera_linea_para_cancelar_ingresos(monkeypatch):

    from application.services import cierre_contable_service

    monkeypatch.setattr(
        cierre_contable_service,
        "ListarEstadoResultados",
        lambda *args, **kwargs: EstadoResultadosIngresoStub(),
    )

    service = CierreContableService(
        MovimientoServiceStub(),
        CuentaServiceIngresoStub(),
    )

    lineas = service.calcular_cierre()

    assert len(lineas) == 2

    assert lineas[0]["cuenta_id"] == 1
    assert lineas[0]["debito"] == Decimal("1000")
    assert lineas[0]["credito"] == Decimal("0")

class CuentaServiceGastoStub:

    def listar(
        self,
    ):
        return [
            CuentaStub(
                13,
                "5.3.01",
                TipoCuenta.GASTO,
            ),
            CuentaStub(
                8,
                "3.2.01",
                TipoCuenta.PATRIMONIO,
            ),
        ]

    def buscar_por_id(
        self,
        cuenta_id,
    ):

        for cuenta in self.listar():

            if cuenta.id == cuenta_id:
                return cuenta

        return None


class EstadoResultadosGastoStub:

    def execute(
        self,
    ):
        return {
            "ingresos": [],
            "egresos": [
                {
                    "cuenta_id": 13,
                    "saldo": Decimal("500"),
                    "debitos": Decimal("500"),
                    "creditos": Decimal("0"),
                }
            ],
            "total_ingresos": Decimal("0"),
            "total_egresos": Decimal("500"),
            "resultado": Decimal("-500"),
        }


def test_genera_linea_para_cancelar_gastos(monkeypatch):

    from application.services import cierre_contable_service

    monkeypatch.setattr(
        cierre_contable_service,
        "ListarEstadoResultados",
        lambda *args, **kwargs: EstadoResultadosGastoStub(),
    )

    service = CierreContableService(
        MovimientoServiceStub(),
        CuentaServiceGastoStub(),
    )

    lineas = service.calcular_cierre()

    assert len(lineas) == 2

    assert lineas[0]["cuenta_id"] == 13
    assert lineas[0]["debito"] == Decimal("0")
    assert lineas[0]["credito"] == Decimal("500")

def test_resultado_positivo_acredita_resultados_acumulados(monkeypatch):

    from application.services import cierre_contable_service

    monkeypatch.setattr(
        cierre_contable_service,
        "ListarEstadoResultados",
        lambda *args, **kwargs: EstadoResultadosIngresoStub(),
    )

    service = CierreContableService(
        MovimientoServiceStub(),
        CuentaServiceIngresoStub(),
    )

    lineas = service.calcular_cierre()

    resultados = lineas[-1]

    assert resultados["cuenta_id"] == 8
    assert resultados["debito"] == Decimal("0")
    assert resultados["credito"] == Decimal("1000")

class EstadoResultadosPerdidaStub:

    def execute(
        self,
    ):
        return {
            "ingresos": [],
            "egresos": [
                {
                    "cuenta_id": 13,
                    "saldo": Decimal("800"),
                    "debitos": Decimal("800"),
                    "creditos": Decimal("0"),
                }
            ],
            "total_ingresos": Decimal("0"),
            "total_egresos": Decimal("800"),
            "resultado": Decimal("-800"),
        }


def test_resultado_negativo_debita_resultados_acumulados(monkeypatch):

    from application.services import cierre_contable_service

    monkeypatch.setattr(
        cierre_contable_service,
        "ListarEstadoResultados",
        lambda *args, **kwargs: EstadoResultadosPerdidaStub(),
    )

    service = CierreContableService(
        MovimientoServiceStub(),
        CuentaServiceGastoStub(),
    )

    lineas = service.calcular_cierre()

    resultados = lineas[-1]

    assert resultados["cuenta_id"] == 8
    assert resultados["debito"] == Decimal("800")
    assert resultados["credito"] == Decimal("0")



