from datetime import date
from decimal import Decimal

from domain.value_objects.renglon_libro_mayor import RenglonLibroMayor
from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta
from domain.services.libro_mayor import LibroMayor


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
        codigo="1.1.02",
        nombre="Banco",
        tipo=TipoCuenta.ACTIVO,
    )
def test_libro_mayor_devuelve_las_lineas_de_una_cuenta():

    caja = crear_cuenta()

    banco = Cuenta(
        id=None,
        empresa_id=1,
        codigo="1.1.02",
        nombre="Banco",
        tipo=TipoCuenta.ACTIVO,
    )

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Transferencia"
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000")
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=banco,
            importe=Decimal("1000")
        )
    )

    movimiento.confirmar()

    libro = LibroMayor() # todavia no existe, luego el test fallará

    lineas = libro.obtener(
        cuenta=caja,
        movimientos=[movimiento]
    )

    assert len(lineas) == 1
    assert lineas[0].cuenta is caja

def test_libro_mayor_devuelve_las_lineas_ordenadas_por_fecha():

    caja = crear_cuenta()

    banco = Cuenta(
        id=None,
        empresa_id=1,
        codigo="1.1.02",
        nombre="Banco",
        tipo=TipoCuenta.ACTIVO,
    )

    movimiento_5 = Movimiento(
        id=None,
        fecha=date(2026, 1, 5),
        descripcion="Movimiento del día 5"
    )

    movimiento_5.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("100")
        )
    )

    movimiento_5.agregar_linea(
        LineaMovimiento.credito(
            cuenta=banco,
            importe=Decimal("100")
        )
    )

    movimiento_5.confirmar()

    movimiento_2 = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Movimiento del día 2"
    )

    movimiento_2.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("200")
        )
    )

    movimiento_2.agregar_linea(
        LineaMovimiento.credito(
            cuenta=banco,
            importe=Decimal("200")
        )
    )

    movimiento_2.confirmar()

    libro = LibroMayor()

    lineas = libro.obtener(
        cuenta=caja,
        movimientos=[
            movimiento_5,
            movimiento_2
        ]
    )

    assert lineas[0].importe == Decimal("200") # El test pide que se devuelva ordenado por fecha
    assert lineas[1].importe == Decimal("100") # La devolucion es como fue la entrada => test 1 fallo
    # linea necesita saber de que movimiento proviene, solo el movimiento tiene fecha, para que se pueda ordenar x fecha

def test_libro_mayor_conserva_fecha_y_descripcion_del_movimiento():
    """
    El Libro Mayor conserva la información cronológica
    y contextual de cada asiento.
    """

    cuenta = crear_cuenta()

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 1, 15),
        descripcion="Cobro de cliente"
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=cuenta,
            importe=Decimal("1500")
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=crear_otra_cuenta(),
            importe=Decimal("1500")
        )
    )

    movimiento.confirmar()

    libro = LibroMayor()

    lineas = libro.obtener(
        cuenta=cuenta,
        movimientos=[movimiento]
    )

    assert len(lineas) == 1

    linea = lineas[0]

    assert linea.movimiento.fecha == date(2026, 1, 15)
    assert linea.movimiento.descripcion == "Cobro de cliente"

def test_libro_mayor_calcula_el_saldo_acumulado():
    """
    El Libro Mayor debe informar el saldo acumulado
    luego de cada movimiento de la cuenta.
    """

    cuenta = crear_cuenta()

    # Primer movimiento (+1000)
    apertura = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Apertura"
    )

    apertura.agregar_linea(
        LineaMovimiento.debito(
            cuenta=cuenta,
            importe=Decimal("1000")
        )
    )

    apertura.agregar_linea(
        LineaMovimiento.credito(
            cuenta=crear_otra_cuenta(),
            importe=Decimal("1000")
        )
    )

    apertura.confirmar()

    # Segundo movimiento (-300)
    pago = Movimiento(
        id=None,
        fecha=date(2026, 1, 5),
        descripcion="Pago"
    )

    pago.agregar_linea(
        LineaMovimiento.credito(
            cuenta=cuenta,
            importe=Decimal("300")
        )
    )

    pago.agregar_linea(
        LineaMovimiento.debito(
            cuenta=crear_otra_cuenta(),
            importe=Decimal("300")
        )
    )

    pago.confirmar()

    libro = LibroMayor()

    lineas = libro.obtener(
        cuenta=cuenta,
        movimientos=[apertura, pago]
    )

    assert len(lineas) == 2

    assert lineas[0].saldo == Decimal("1000")
    assert lineas[1].saldo == Decimal("700")


def test_libro_mayor_devuelve_renglones():

    cuenta = crear_cuenta()

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Apertura"
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=cuenta,
            importe=Decimal("1000")
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=crear_otra_cuenta(),
            importe=Decimal("1000")
        )
    )

    movimiento.confirmar()

    libro = LibroMayor()

    renglones = libro.obtener(
        cuenta=cuenta,
        movimientos=[movimiento]
    )

    assert len(renglones) == 1

    assert isinstance(
        renglones[0],
        RenglonLibroMayor
    )