from infrastructure.mappers.cuenta_mapper import (
    CuentaMapper,
)

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta


def test_mapper_convierte_entidad_a_dict():

    cuenta = Cuenta(
        id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    datos = CuentaMapper.to_dict(
        cuenta,
    )

    assert datos == {
        "id": 1,
        "codigo": "1.1.01",
        "nombre": "Caja",
        "tipo": "ACTIVO",
        "activa": True,
    }

from domain.enums.tipo_cuenta import TipoCuenta


def test_mapper_convierte_dict_a_entidad():

    datos = {
        "id": 1,
        "codigo": "1.1.01",
        "nombre": "Caja",
        "tipo": "ACTIVO",
        "activa": True,
    }

    cuenta = CuentaMapper.from_dict(
        datos,
    )

    assert cuenta.id == 1
    assert cuenta.codigo == "1.1.01"
    assert cuenta.nombre == "Caja"
    assert cuenta.tipo == TipoCuenta.ACTIVO
    assert cuenta.activa is True

def test_mapper_convierte_lista_de_entidades_a_lista_de_dict():

    cuenta1 = Cuenta(
        id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    cuenta2 = Cuenta(
        id=2,
        codigo="2.1.01",
        nombre="Proveedores",
        tipo=TipoCuenta.PASIVO,
    )

    datos = CuentaMapper.to_dict_list(
        [
            cuenta1,
            cuenta2,
        ]
    )

    assert datos == [
        {
            "id": 1,
            "codigo": "1.1.01",
            "nombre": "Caja",
            "tipo": "ACTIVO",
            "activa": True,
        },
        {
            "id": 2,
            "codigo": "2.1.01",
            "nombre": "Proveedores",
            "tipo": "PASIVO",
            "activa": True,
        },
    ]

def test_mapper_convierte_lista_de_dict_a_lista_de_entidades():

    datos = [
        {
            "id": 1,
            "codigo": "1.1.01",
            "nombre": "Caja",
            "tipo": "ACTIVO",
            "activa": True,
        },
        {
            "id": 2,
            "codigo": "2.1.01",
            "nombre": "Proveedores",
            "tipo": "PASIVO",
            "activa": True,
        },
    ]

    cuentas = CuentaMapper.from_dict_list(
        datos,
    )

    assert len(cuentas) == 2

    assert cuentas[0].codigo == "1.1.01"
    assert cuentas[0].tipo == TipoCuenta.ACTIVO

    assert cuentas[1].codigo == "2.1.01"
    assert cuentas[1].tipo == TipoCuenta.PASIVO
