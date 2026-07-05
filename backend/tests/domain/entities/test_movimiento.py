from datetime import date
from decimal import Decimal

import pytest


from domain.enums.tipo_afectacion import TipoAfectacion
from domain.enums.estado_movimiento import EstadoMovimiento
from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta


def crear_cuenta() -> Cuenta:
    return Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )


def test_agregar_una_linea():
    """
    Un movimiento debe poder agregar una línea.
    """

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra de medicamentos"
        
    )

    linea = LineaMovimiento(
        cuenta=crear_cuenta(),
        importe=Decimal("1000"),
        tipo_afectacion=TipoAfectacion.DEBITO
    )
    movimiento.agregar_linea(linea)
    movimiento.agregar_linea(
    LineaMovimiento(
        cuenta=crear_cuenta(),
        importe=Decimal("1000"),
        tipo_afectacion=TipoAfectacion.CREDITO
    )
    )
    assert len(movimiento.lineas) == 2
    assert movimiento.lineas[0] == linea
    
    movimiento.confirmar()

    assert movimiento.estado == EstadoMovimiento.CONFIRMADO

def test_cantidad_lineas():
    """
    Un movimiento debe informar correctamente
    la cantidad de líneas que contiene.
    """

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra de medicamentos"
    )

    assert movimiento.cantidad_lineas() == 0

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000"),
            tipo_afectacion=TipoAfectacion.DEBITO
        )
    )

    assert movimiento.cantidad_lineas() == 1

def test_movimiento_tiene_lineas():
    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra"
    )

    assert movimiento.tiene_lineas() is False

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000"),
            tipo_afectacion=TipoAfectacion.DEBITO
        )
    )

    assert movimiento.tiene_lineas() is True

def test_movimiento_nace_en_borrador():
    """
    Todo movimiento recién creado debe iniciar
    en estado BORRADOR.
    """

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra de medicamentos"
    )

    assert movimiento.esta_en_borrador() is True

def test_confirmar_movimiento():
    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra de medicamentos"
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000"),
            tipo_afectacion=TipoAfectacion.DEBITO
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000"),
            tipo_afectacion=TipoAfectacion.CREDITO
        )
    )

    movimiento.confirmar()

    assert movimiento.estado == EstadoMovimiento.CONFIRMADO
    
def test_no_se_puede_confirmar_un_movimiento_sin_lineas():
    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra"
    )

    with pytest.raises(ValueError):
        movimiento.confirmar()


def test_no_se_pueden_agregar_lineas_a_un_movimiento_confirmado():
    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra"
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000"),
            tipo_afectacion=TipoAfectacion.DEBITO
        )
    )
    movimiento.agregar_linea(
    LineaMovimiento(
        cuenta=crear_cuenta(),
        importe=Decimal("1000"),
        tipo_afectacion=TipoAfectacion.CREDITO
    )
)

    movimiento.confirmar()

    with pytest.raises(ValueError):
        movimiento.agregar_linea(
            LineaMovimiento(
                cuenta=crear_cuenta(),
                importe=Decimal("500"),
                tipo_afectacion=TipoAfectacion.DEBITO   
            )
        )        

def test_total_debitos():
    """
    Un movimiento debe poder calcular
    la suma de todos sus débitos.
    """

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra de medicamentos"
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000"),
            tipo_afectacion=TipoAfectacion.DEBITO
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("250"),
            tipo_afectacion=TipoAfectacion.DEBITO
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("900"),
            tipo_afectacion=TipoAfectacion.CREDITO
        )
    )

    assert movimiento.total_debitos() == Decimal("1250")

def test_total_creditos():
    """
    Un movimiento debe calcular
    correctamente la suma de sus créditos.
    """

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra"
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("300"),
            tipo_afectacion=TipoAfectacion.DEBITO
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("700"),
            tipo_afectacion=TipoAfectacion.CREDITO
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("500"),
            tipo_afectacion=TipoAfectacion.CREDITO
        )
    )

    assert movimiento.total_creditos() == Decimal("1200")

def test_movimiento_balanceado():
    """
    Un movimiento está balanceado
    cuando los débitos igualan a los créditos.
    """

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra"
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000"),
            tipo_afectacion=TipoAfectacion.DEBITO
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000"),
            tipo_afectacion=TipoAfectacion.CREDITO
        )
    )

    assert movimiento.esta_balanceado() is True

def test_no_se_puede_confirmar_un_movimiento_desbalanceado():
    """
    Un movimiento desbalanceado nunca puede confirmarse.
    """

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra de medicamentos"
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000"),
            tipo_afectacion=TipoAfectacion.DEBITO
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("500"),
            tipo_afectacion=TipoAfectacion.CREDITO
        )
    )

    with pytest.raises(
        ValueError,
        match="movimiento no está balanceado"
    ):
        movimiento.confirmar()