from domain.value_objects.cuit import Cuit


def test_crea_un_cuit():

    cuit = Cuit(
        "30-12345678-9"
    )

    assert cuit.valor == "30-12345678-9"


import pytest


def test_no_permite_cuit_con_longitud_incorrecta():

    with pytest.raises(ValueError):

        Cuit("123")