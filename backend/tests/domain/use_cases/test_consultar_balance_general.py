from domain.use_cases.consultar_balance_general import ConsultarBalanceGeneral
from tests.builders.movimientos_builder import crear_movimientos_del_ejercicio


def test_devuelve_un_balance_general_calculado():

    caso = ConsultarBalanceGeneral()

    balance = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    from domain.value_objects.balance_general_calculado import (
        BalanceGeneralCalculado,
    )

    assert isinstance(
        balance,
        BalanceGeneralCalculado,
    )