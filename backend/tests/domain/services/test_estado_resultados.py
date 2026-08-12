from datetime import date
from decimal import Decimal


from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta
from domain.services.estado_resultados import EstadoResultados
from domain.value_objects.saldo_cuenta import SaldoCuenta
from tests.builders.entidades_builder import (
    crear_caja,
    crear_ventas,
    crear_gastos,
    crear_ejercicio,
    crear_movimiento_de_venta_confirmado,
    crear_movimiento_de_gasto_confirmado,
)


crear_caja()

crear_ventas()


def test_estado_resultados_informa_las_cuentas_de_ingreso():
    """
    El Estado de Resultados informa
    las cuentas de Ingreso.
    """

    caja = crear_caja()
    ventas = crear_ventas()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 2),
        descripcion="Venta contado",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=ventas,
            importe=Decimal("1000"),
        )
    )

    movimiento.confirmar()

    estado = EstadoResultados()

    ingresos = estado.ingresos(
        movimientos=[movimiento]
    )

    assert len(ingresos) == 1

    assert ingresos[0].cuenta is ventas
    assert ingresos[0].saldo == Decimal("1000")

    crear_gastos()



def test_estado_resultados_informa_las_cuentas_de_gasto():
    """
    El Estado de Resultados informa
    las cuentas de Gasto.
    """

    caja = crear_caja()
    gasto = crear_gastos()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 2),
        descripcion="Pago de alquiler",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=gasto,
            importe=Decimal("300"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=caja,
            importe=Decimal("300"),
        )
    )

    movimiento.confirmar()

    estado = EstadoResultados()

    gastos = estado.gastos(
        movimientos=[movimiento]
    )

    assert len(gastos) == 1

    assert gastos[0].cuenta is gasto
    assert gastos[0].saldo == Decimal("300")

def test_estado_resultados_informa_el_total_de_ingresos():
    """
    El Estado de Resultados informa
    el total de Ingresos.
    """

    caja = crear_caja()
    ventas = crear_ventas()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 2),
        descripcion="Venta contado",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=ventas,
            importe=Decimal("1000"),
        )
    )

    movimiento.confirmar()

    estado = EstadoResultados()

    assert estado.total_ingresos(
        movimientos=[movimiento]
    ) == Decimal("1000")

def test_estado_resultados_informa_el_total_de_gastos():
    """
    El Estado de Resultados informa
    el total de Gastos.
    """

    caja = crear_caja()
    gasto = crear_gastos()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 2),
        descripcion="Pago de alquiler",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=gasto,
            importe=Decimal("300"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=caja,
            importe=Decimal("300"),
        )
    )

    movimiento.confirmar()

    estado = EstadoResultados()

    assert estado.total_gastos(
        movimientos=[movimiento]
    ) == Decimal("300")


def test_estado_resultados_informa_los_saldos_de_las_cuentas():
    """
    El Estado de Resultados informa
    el saldo de cada cuenta de resultado.
    """
    caja = crear_caja()
    ventas = crear_ventas()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 6, 1),
        descripcion="Venta",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=ventas,
            importe=Decimal("1000"),
        )
    )

    movimiento.confirmar()

    estado = EstadoResultados()

    saldos = estado.saldos(
        movimientos=[movimiento],
    )

    assert len(saldos) == 1

    saldo = saldos[0]

    assert isinstance(
        saldo,
        SaldoCuenta,
    )

    assert saldo.cuenta == ventas

    assert saldo.saldo == Decimal("1000")

def test_estado_resultados_agrupa_los_saldos_de_una_misma_cuenta():
        """
        Los movimientos de una misma cuenta
        generan un único saldo acumulado.
        """

        movimiento1 = crear_movimiento_de_venta_confirmado(
            Decimal("1000")
        )

        movimiento2 = crear_movimiento_de_venta_confirmado(
            Decimal("500")
        )

        estado = EstadoResultados()

        saldos = estado.saldos(
            movimientos=[
                movimiento1,
                movimiento2,
            ],
        )

        assert len(saldos) == 1

        saldo = saldos[0]

        assert saldo.cuenta.nombre == "Ventas"

        assert saldo.saldo == Decimal("1500")

def test_estado_resultados_informa_los_saldos_de_las_cuentas_de_gasto():
    """
    El Estado de Resultados también informa
    los saldos de las cuentas de gasto.
    """

    movimiento = crear_movimiento_de_gasto_confirmado()
    estado = EstadoResultados()

    saldos = estado.saldos(
        movimientos=[movimiento],
    )

    assert len(saldos) == 1

    saldo = saldos[0]

    assert saldo.cuenta.tipo == TipoCuenta.GASTO

    assert saldo.saldo == Decimal("300")

    crear_gastos()


crear_movimiento_de_gasto_confirmado()

def test_estado_resultados_calcula_el_resultado_del_ejercicio():
    """
    El Estado de Resultados calcula
    el resultado del ejercicio.
    """

    movimiento_ingreso = crear_movimiento_de_venta_confirmado(
        Decimal("1000")
    )

    movimiento_gasto = crear_movimiento_de_gasto_confirmado(
        Decimal("300")
    )

    estado = EstadoResultados()

    resultado = estado.resultado(
        movimientos=[
            movimiento_ingreso,
            movimiento_gasto,
        ],
    )

    assert resultado == Decimal("700")

def test_estado_resultados_puede_generar_un_estado_calculado():
    """
    El servicio puede devolver un EstadoResultadosCalculado.
    """

    movimiento = crear_movimiento_de_venta_confirmado()

    estado = EstadoResultados()

    calculado = estado.calcular(
        movimientos=[movimiento],
    )

    assert calculado.resultado == Decimal("1000")
    assert len(calculado.saldos) == 1