from domain.entities.empresa import Empresa
from domain.value_objects.cuit import Cuit


def test_crear_empresa():

    empresa = Empresa(
        id=None,
        razon_social="Acme S.A.",
        nombre_fantasia="Acme",
        cuit="30-12345678-9",
    )

    assert empresa.razon_social == "Acme S.A."
    assert empresa.nombre_fantasia == "Acme"
    assert empresa.cuit == "30-12345678-9"
    assert empresa.activa is True

def test_empresa_nace_activa():

    empresa = Empresa(
        id=None,
        razon_social="Acme S.A.",
        nombre_fantasia="Acme",
        cuit="30-12345678-9",
    )

    assert empresa.activa is True

def test_desactivar_empresa():

    empresa = Empresa(
        id=None,
        razon_social="Acme S.A.",
        nombre_fantasia="Acme",
        cuit="30-12345678-9",
    )

    empresa.desactivar()

    assert empresa.activa is False

def test_activar_empresa():

    empresa = Empresa(
        id=None,
        razon_social="Acme S.A.",
        nombre_fantasia="Acme",
        cuit="30-12345678-9",
    )

    empresa.desactivar()

    empresa.activar()

    assert empresa.activa is True

import pytest


def test_empresa_no_permite_razon_social_vacia():

    with pytest.raises(ValueError):

        Empresa(
            id=None,
            razon_social="",
            nombre_fantasia="Acme",
            cuit="30-12345678-9",
        )

def test_empresa_no_permite_nombre_fantasia_vacio():

    with pytest.raises(ValueError):

        Empresa(
            id=None,
            razon_social="Acme S.A.",
            nombre_fantasia="",
            cuit="30-12345678-9",
        )
def test_empresa_no_permite_cuit_vacio():

    with pytest.raises(ValueError):

        Empresa(
            id=None,
            razon_social="Acme S.A.",
            nombre_fantasia="Acme",
            cuit="",
        )

def test_empresa_no_permite_cuit_invalido():

    with pytest.raises(ValueError):

        Empresa(
            id=None,
            razon_social="Acme S.A.",
            nombre_fantasia="Acme",
            cuit="123",
        )

def test_normaliza_cuit_sin_guiones():

    cuit = Cuit(
        "30123456789"
    )

    assert cuit.valor == "30-12345678-9"