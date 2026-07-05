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