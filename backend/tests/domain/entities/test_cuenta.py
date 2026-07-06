from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta


def test_cuenta_nace_activa():
    """
    Toda cuenta nueva nace activa.
    """

    cuenta = Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    assert cuenta.activa is True

def test_cuenta_nace_imputable():
    """
    Una cuenta nueva nace como imputable.
    """

    cuenta = Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO
    )

    assert cuenta.imputable is True

def test_hacer_no_imputable():
    """
    Una cuenta puede dejar de ser imputable.
    """

    cuenta = Cuenta(
        id=None,
        codigo="1",
        nombre="Activo",
        tipo=TipoCuenta.ACTIVO
    )

    cuenta.hacer_no_imputable()

    assert cuenta.imputable is False

def test_hacer_imputable():
    """
    Una cuenta puede volver a ser imputable.
    """

    cuenta = Cuenta(
        id=None,
        codigo="1",
        nombre="Activo",
        tipo=TipoCuenta.ACTIVO
    )

    cuenta.hacer_no_imputable()
    cuenta.hacer_imputable()

    assert cuenta.imputable is True

def test_es_imputable():
    """
    Una cuenta debe informar si es imputable.
    """

    cuenta = Cuenta(
        id=None,
        codigo="1",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO
    )

    assert cuenta.es_imputable() is True

    cuenta.hacer_no_imputable()

    assert cuenta.es_imputable() is False