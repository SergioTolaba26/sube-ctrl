from domain.use_cases.consultar_balance_sumas_saldos import (
    ConsultarBalanceSumasSaldos,
)

from tests.builders.movimientos_builder import (
    crear_movimientos_del_ejercicio,
)
from decimal import Decimal


def test_devuelve_las_filas_del_balance():

    caso = ConsultarBalanceSumasSaldos()

    filas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert len(filas) > 0

def test_devuelve_seis_cuentas():

    caso = ConsultarBalanceSumasSaldos()

    filas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert len(filas) == 6



def test_la_primer_fila_corresponde_a_caja():

    caso = ConsultarBalanceSumasSaldos()

    filas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert filas[0].cuenta.nombre == "Caja"
    assert filas[0].saldo == Decimal("500")

def test_la_segunda_fila_corresponde_a_ventas():

    caso = ConsultarBalanceSumasSaldos()

    filas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert filas[1].cuenta.nombre == "Ventas"
    assert filas[1].saldo == Decimal("1000")

def test_la_tercer_fila_corresponde_a_compras():

    caso = ConsultarBalanceSumasSaldos()

    filas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert filas[2].cuenta.nombre == "Compras"
    assert filas[2].saldo == Decimal("500")

def test_la_cuarta_fila_corresponde_a_gastos_administrativos():

    caso = ConsultarBalanceSumasSaldos()

    filas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert (
        filas[3].cuenta.nombre
        == "Gastos Administrativos"
    )

    assert filas[3].saldo == Decimal("300")

def test_la_quinta_fila_corresponde_a_proveedores():

    caso = ConsultarBalanceSumasSaldos()

    filas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert filas[4].cuenta.nombre == "Proveedores"
    
    assert filas[4].saldo == Decimal("-500")

def test_la_sexta_fila_corresponde_a_clientes():

    caso = ConsultarBalanceSumasSaldos()

    filas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert filas[5].cuenta.nombre == "Clientes"
    assert filas[5].saldo == Decimal("-800")


 
from domain.use_cases.consultar_balance_general import (
    ConsultarBalanceGeneral,
)

from tests.builders.movimientos_builder import (
    crear_movimientos_del_ejercicio,
)


def test_devuelve_un_balance_general():

    caso = ConsultarBalanceGeneral()

    balance = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert balance is not None   
from domain.services.balance_general import (
    BalanceGeneral,
)



from domain.services.balance_general import (
    BalanceGeneral,
)


def test_devuelve_total_activos():

    caso = ConsultarBalanceGeneral()

    balance = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )
    assert balance.total_activos == Decimal("-300")

def test_devuelve_total_pasivos():

    caso = ConsultarBalanceGeneral()

    balance = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert balance.total_pasivos == Decimal("-500")

def test_devuelve_total_patrimonio():

    caso = ConsultarBalanceGeneral()

    balance = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert balance.total_patrimonio == Decimal("0")