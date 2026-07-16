from persistence.repositories.plan_cuenta_repository_json import (
    PlanCuentaRepositoryJson,
)

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta


def test_convierte_cuenta_a_dict():

    repo = PlanCuentaRepositoryJson()

    cuenta = Cuenta(
        id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    data = repo._to_dict(cuenta)

    assert data == {

        "id": 1,

        "codigo": "1.1.01",

        "nombre": "Caja",

        "tipo": "ACTIVO",

        "activa": True,

    }

def test_busca_cuenta_por_codigo(tmp_path):

    archivo = tmp_path / "plan_cuentas.json"

    archivo.write_text(
        '{"cuentas": []}',
        encoding="utf-8",
    )

    repo = PlanCuentaRepositoryJson(
        archivo,
    )

    cuenta = Cuenta(
        id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    repo.guardar(cuenta)

    encontrada = repo.buscar_por_codigo(
        "1.1.01"
    )

    assert encontrada is not None

    assert encontrada.codigo == "1.1.01"

    assert encontrada.nombre == "Caja"

def test_busca_cuenta_por_codigo_inexistente(tmp_path):

    archivo = tmp_path / "plan_cuentas.json"

    archivo.write_text(
        '{"cuentas": []}',
        encoding="utf-8",
    )

    repo = PlanCuentaRepositoryJson(
        archivo,
    )

    cuenta = Cuenta(
        id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    repo.guardar(cuenta)

    encontrada = repo.buscar_por_codigo(
        "9.9.99"
    )

    assert encontrada is None