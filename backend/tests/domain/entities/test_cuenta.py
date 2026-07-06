import pytest
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

def test_asignar_cuenta_padre():
    """
    Una cuenta puede pertenecer a otra cuenta.
    """

    padre = Cuenta(
        id=None,
        codigo="1.1",
        nombre="Bancos",
        tipo=TipoCuenta.ACTIVO,
    )

    hija = Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Banco Nación",
        tipo=TipoCuenta.ACTIVO,
    )

    hija.asignar_padre(padre)

    assert hija.padre == padre    

def test_al_asignar_un_hijo_la_cuenta_padre_deja_de_ser_imputable():
    padre = Cuenta(
        id=None,
        codigo="1",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO
    )

    hija = Cuenta(
        id=None,
        codigo="1.1",
        nombre="Caja Principal",
        tipo=TipoCuenta.ACTIVO
    )

    assert padre.es_imputable() is True

    hija.asignar_padre(padre)

    assert padre.es_imputable() is False

def test_la_cuenta_padre_conoce_a_sus_hijos():
    """
    Al asignar un padre, éste debe registrar
    automáticamente a la cuenta hija.
    """

    padre = Cuenta(
        id=None,
        codigo="1",
        nombre="Activo",
        tipo=TipoCuenta.ACTIVO,
    )

    hija = Cuenta(
        id=None,
        codigo="1.1",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    hija.asignar_padre(padre)

    assert hija in padre.hijos
    
def test_no_se_puede_cambiar_de_padre():
    """
    Una cuenta no puede pertenecer a dos padres.
    """

    padre1 = Cuenta(
        id=None,
        codigo="1",
        nombre="Activo",
        tipo=TipoCuenta.ACTIVO,
    )

    padre2 = Cuenta(
        id=None,
        codigo="2",
        nombre="Pasivo",
        tipo=TipoCuenta.PASIVO,
    )

    hija = Cuenta(
        id=None,
        codigo="1.1",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    hija.asignar_padre(padre1)

    with pytest.raises(
        ValueError,
        match="ya tiene una cuenta padre"
    ):
        hija.asignar_padre(padre2)

def test_obtener_ancestros():
    """
    Una cuenta debe poder obtener todos sus ancestros
    desde el padre inmediato hasta la raíz.
    """

    raiz = Cuenta(
        id=None,
        codigo="1",
        nombre="Activo",
        tipo=TipoCuenta.ACTIVO,
    )

    padre = Cuenta(
        id=None,
        codigo="1.1",
        nombre="Bancos",
        tipo=TipoCuenta.ACTIVO,
    )

    hija = Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Banco Nación",
        tipo=TipoCuenta.ACTIVO,
    )

    padre.asignar_padre(raiz)
    hija.asignar_padre(padre)

    assert hija.ancestros() == [padre, raiz]

def test_no_se_puede_generar_un_ciclo():
    """
    El árbol del plan de cuentas nunca puede contener ciclos.
    """

    raiz = Cuenta(
        id=None,
        codigo="1",
        nombre="Activo",
        tipo=TipoCuenta.ACTIVO,
    )

    padre = Cuenta(
        id=None,
        codigo="1.1",
        nombre="Bancos",
        tipo=TipoCuenta.ACTIVO,
    )

    hija = Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Banco Nación",
        tipo=TipoCuenta.ACTIVO,
    )

    padre.asignar_padre(raiz)
    hija.asignar_padre(padre)

    with pytest.raises(
        ValueError,
        match="ciclo"
    ):
        raiz.asignar_padre(hija)

def test_obtener_descendientes():
    """
    Una cuenta debe poder obtener todos sus
    descendientes.
    """

    raiz = Cuenta(
        id=None,
        codigo="1",
        nombre="Activo",
        tipo=TipoCuenta.ACTIVO,
    )

    bancos = Cuenta(
        id=None,
        codigo="1.1",
        nombre="Bancos",
        tipo=TipoCuenta.ACTIVO,
    )

    caja = Cuenta(
        id=None,
        codigo="1.2",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    nacion = Cuenta(
        id=None,
        codigo="1.1.1",
        nombre="Banco Nación",
        tipo=TipoCuenta.ACTIVO,
    )

    bancos.asignar_padre(raiz)
    caja.asignar_padre(raiz)
    nacion.asignar_padre(bancos)

    assert raiz.descendientes() == [
        bancos,
        nacion,
        caja,
    ]

def test_una_cuenta_sin_hijos_es_hoja():
    """
    Una cuenta sin hijos debe ser una hoja.
    """

    cuenta = Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    assert cuenta.es_hoja() is True

def test_nivel_de_una_cuenta():
    """
    Una cuenta debe conocer el nivel que ocupa
    dentro del plan de cuentas.
    """

    raiz = Cuenta(
        id=None,
        codigo="1",
        nombre="Activo",
        tipo=TipoCuenta.ACTIVO,
    )

    padre = Cuenta(
        id=None,
        codigo="1.1",
        nombre="Bancos",
        tipo=TipoCuenta.ACTIVO,
    )

    hija = Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Banco Nación",
        tipo=TipoCuenta.ACTIVO,
    )

    padre.asignar_padre(raiz)
    hija.asignar_padre(padre)

    assert raiz.nivel() == 0
    assert padre.nivel() == 1
    assert hija.nivel() == 2

def test_ruta_de_una_cuenta():
    """
    Una cuenta debe conocer su ruta
    desde la raíz.
    """

    activo = Cuenta(
        id=None,
        codigo="1",
        nombre="Activo",
        tipo=TipoCuenta.ACTIVO,
    )

    bancos = Cuenta(
        id=None,
        codigo="1.1",
        nombre="Bancos",
        tipo=TipoCuenta.ACTIVO,
    )

    nacion = Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Banco Nación",
        tipo=TipoCuenta.ACTIVO,
    )

    bancos.asignar_padre(activo)
    nacion.asignar_padre(bancos)

    assert nacion.ruta() == [
        activo,
        bancos,
        nacion,
    ]