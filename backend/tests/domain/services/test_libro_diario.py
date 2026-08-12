from datetime import date
from decimal import Decimal

from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta
from domain.services.libro_diario import LibroDiario
from domain.services.asiento_libro_diario import AsientoLibroDiario

def crear_cuenta():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )


def crear_otra_cuenta():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="3.1.01",
        nombre="Capital",
        tipo=TipoCuenta.PATRIMONIO,
    )


def test_libro_diario_devuelve_movimientos_confirmados_ordenados_por_fecha():
    """
    El Libro Diario devuelve los movimientos confirmados
    ordenados cronológicamente.
    """

    cuenta = crear_cuenta()
    contrapartida = crear_otra_cuenta()

    movimiento_5 = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 5),
        descripcion="Movimiento del día 5",
    )

    movimiento_5.agregar_linea(
        LineaMovimiento.debito(
            cuenta=cuenta,
            importe=Decimal("100"),
        )
    )

    movimiento_5.agregar_linea(
        LineaMovimiento.credito(
            cuenta=contrapartida,
            importe=Decimal("100"),
        )
    )

    movimiento_5.confirmar()

    movimiento_2 = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 2),
        descripcion="Movimiento del día 2",
    )

    movimiento_2.agregar_linea(
        LineaMovimiento.debito(
            cuenta=cuenta,
            importe=Decimal("200"),
        )
    )

    movimiento_2.agregar_linea(
        LineaMovimiento.credito(
            cuenta=contrapartida,
            importe=Decimal("200"),
        )
    )

    movimiento_2.confirmar()

    diario = LibroDiario()

    asientos = diario.obtener([
        movimiento_5,
        movimiento_2,
    ])

    assert len(asientos) == 2
    assert asientos[0].movimiento.fecha == date(2026, 1, 2)
    assert asientos[1].movimiento.fecha == date(2026, 1, 5)




def test_libro_diario_devuelve_asientos():
    """
    El Libro Diario devuelve objetos AsientoLibroDiario
    en lugar de exponer directamente los Movimientos.
    """

    cuenta = crear_cuenta()
    contrapartida = crear_otra_cuenta()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 2),
        descripcion="Apertura",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=cuenta,
            importe=Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=contrapartida,
            importe=Decimal("1000"),
        )
    )

    movimiento.confirmar()

    diario = LibroDiario()

    asientos = diario.obtener([
        movimiento,
    ])

    assert len(asientos) == 1

    assert isinstance(
        asientos[0],
        AsientoLibroDiario,
    )

    assert asientos[0].movimiento is movimiento 

def test_asiento_libro_diario_expone_la_fecha_del_movimiento():
    """
    Un AsientoLibroDiario expone la fecha
    de su movimiento.
    """

    movimiento = Movimiento(
        
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 15),
        descripcion="Cobro"
    )

    asiento = AsientoLibroDiario(
        movimiento=movimiento
    )

    assert asiento.fecha == date(2026, 1, 15)