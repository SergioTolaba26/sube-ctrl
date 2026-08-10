from application.use_cases import cuenta
from infrastructure.persistence.base.storage import (
    Storage,
)

from infrastructure.repositories.json.cuenta_repository import (
    CuentaRepositoryJson,
)
from tests.factories.cuenta_factory import CuentaFactory


def test_crea_repositorio(tmp_path):

    storage = Storage(
        tmp_path / "cuentas.json",
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    assert repository.storage is storage

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta


def test_listar_devuelve_lista_de_cuentas(
    tmp_path,
):

    storage = Storage(
        tmp_path / "cuentas.json",
    )

    storage.save(
        [
            {
                "id": 1,
                "empresa_id": 1,
                "codigo": "1.1.01",
                "nombre": "Caja",
                "tipo": "ACTIVO",
                "activa": True,
            },
            {
                "id": 2,
                "empresa_id": 1,
                "codigo": "2.1.01",
                "nombre": "Proveedores",
                "tipo": "PASIVO",
                "activa": True,
            },
        ]
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    cuentas = repository.listar()

    assert len(cuentas) == 2

    assert isinstance(
        cuentas[0],
        Cuenta,
    )

    assert cuentas[0].codigo == "1.1.01"
    assert cuentas[1].codigo == "2.1.01"


def test_buscar_por_codigo_devuelve_la_cuenta(
    tmp_path,
):

    storage = Storage(
        tmp_path / "cuentas.json",
    )

    storage.save(
        [
            {
                "id": 1,
                "empresa_id": 1,
                "codigo": "1.1.01",
                "nombre": "Caja",
                "tipo": "ACTIVO",
                "activa": True,
            },
            {
                "id": 2,
                "empresa_id": 1,
                "codigo": "2.1.01",
                "nombre": "Proveedores",
                "tipo": "PASIVO",
                "activa": True,
            },
        ]
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    cuenta = repository.buscar_por_codigo(
        "2.1.01",
    )

    assert cuenta is not None

    assert cuenta.codigo == "2.1.01"

    assert cuenta.nombre == "Proveedores"

    assert cuenta.tipo == TipoCuenta.PASIVO

def test_buscar_por_codigo_devuelve_none_si_no_existe(
    tmp_path,
):

    storage = Storage(
        tmp_path / "cuentas.json",
    )

    storage.save(
        [
            {
                "id": 1,
                "empresa_id": 1,
                "codigo": "1.1.01",
                "nombre": "Caja",
                "tipo": "ACTIVO",
                "activa": True,
            },
        ]
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    cuenta = repository.buscar_por_codigo(
        "9.9.99",
    )

    assert cuenta is None

def test_guardar_agrega_una_cuenta(
    tmp_path,
):

    storage = Storage(
        tmp_path / "cuentas.json",
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    # cuenta = Cuenta(
    #     id=1,
    empresa_id=1,
    #     codigo="1.1.01",
    #     nombre="Caja",
    #     tipo=TipoCuenta.ACTIVO,
    # )
  
    cuenta = CuentaFactory.crear()
    # Si deseo ampliar o indicar algo mas de la cuenta
    # CuentaFactory.crear(
    # nombre="Caja Principal",
    # )
    repository.guardar(
        cuenta,
    )

    cuentas = repository.listar()

    assert len(cuentas) == 1

    assert cuentas[0].codigo ==     "1.1.01"

    assert cuentas[0].nombre == "Caja"

def test_guardar_actualiza_si_el_id_ya_existe( 
    tmp_path,
):

    storage = Storage(
        tmp_path / "cuentas.json",
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    repository.guardar(
        Cuenta(
            id=1,
            empresa_id=1,
            codigo="1.1.01",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    repository.guardar(
        Cuenta(
            id=1,
            empresa_id=1,
            codigo="1.1.01",
            nombre="Caja Principal",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    cuentas = repository.listar()

    assert len(cuentas) == 1

    assert cuentas[0].nombre == "Caja Principal"

def test_buscar_por_id_devuelve_la_cuenta(
    tmp_path,
):

    storage = Storage(
        tmp_path / "cuentas.json",
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    repository.guardar(
        Cuenta(
            id=10,
            empresa_id=1,
            codigo="1.1.01",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    cuenta = repository.buscar_por_id(
        10,
    )

    assert cuenta is not None

    assert cuenta.id == 10

    assert cuenta.codigo == "1.1.01"

def test_buscar_por_id_devuelve_none_si_no_existe(
    tmp_path,
):

    storage = Storage(
        tmp_path / "cuentas.json",
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    repository.guardar(
        Cuenta(
            id=1,
            empresa_id=1,
            codigo="1.1.01",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    cuenta = repository.buscar_por_id(
        999,
    )

    assert cuenta is None

def test_eliminar_quita_la_cuenta(
    tmp_path,
):

    storage = Storage(
        tmp_path / "cuentas.json",
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    # cuenta = Cuenta(
    #     id=1,
    empresa_id=1,
    #     codigo="1.1.01",
    #     nombre="Caja",
    #     tipo=TipoCuenta.ACTIVO,
    # )
    cuenta = CuentaFactory.crear()

    repository.guardar(
        cuenta,
    )

    repository.eliminar(
        1,
    )

    cuentas = repository.listar()

    assert len(cuentas) == 0

def test_eliminar_id_inexistente_no_hace_nada(
    tmp_path,
):

    storage = Storage(
        tmp_path / "cuentas.json",
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    repository.guardar(
        Cuenta(
            id=1,
            empresa_id=1,
            codigo="1.1.01",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    repository.eliminar(
        999,
    )

    cuentas = repository.listar()

    assert len(cuentas) == 1

    assert cuentas[0].codigo == "1.1.01"

