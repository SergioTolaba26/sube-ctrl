from infrastructure.persistence.base.storage import (
    Storage,
)

from infrastructure.repositories.json.cuenta_repository import (
    CuentaRepositoryJson,
)

from tests.factories.cuenta_factory import (
    CuentaFactory,
)

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta


def test_crea_repositorio(tmp_path):

    storage = Storage(
        tmp_path / "cuentas.json",
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    assert repository.storage is storage


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
            {
                "id": 3,
                "empresa_id": 2,
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

    cuentas = repository.listar(
        empresa_id=1,
    )

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
        empresa_id=1,
        codigo="2.1.01",
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
        empresa_id=1,
        codigo="9.9.99",
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

    cuenta = CuentaFactory.crear()

    repository.guardar(
        cuenta,
    )

    cuentas = repository._listar_todas()

    assert len(cuentas) == 1

    assert cuentas[0].codigo == "1.1.01"

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

    cuentas = repository._listar_todas()

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
        empresa_id=1,
        cuenta_id=10,
    )

    assert cuenta is not None

    assert cuenta.id == 10

    assert cuenta.empresa_id == 1

    assert cuenta.codigo == "1.1.01"


def test_buscar_por_id_no_devuelve_cuenta_de_otra_empresa(
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
        empresa_id=2,
        cuenta_id=10,
    )

    assert cuenta is None


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
        empresa_id=1,
        cuenta_id=999,
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

    cuenta = CuentaFactory.crear()

    repository.guardar(
        cuenta,
    )

    repository.eliminar(
        empresa_id=cuenta.empresa_id,
        cuenta_id=cuenta.id,
    )

    cuentas = repository._listar_todas()

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
        empresa_id=1,
        cuenta_id=999,
    )

    cuentas = repository._listar_todas()

    assert len(cuentas) == 1

    assert cuentas[0].codigo == "1.1.01"

def test_modificar_cambia_la_cuenta_de_la_empresa(
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

    cuenta_modificada = Cuenta(
        id=10,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja Principal",
        tipo=TipoCuenta.ACTIVO,
    )

    repository.modificar(
        empresa_id=1,
        cuenta=cuenta_modificada,
    )

    cuenta = repository.buscar_por_id(
        empresa_id=1,
        cuenta_id=10,
    )

    assert cuenta is not None

    assert cuenta.id == 10

    assert cuenta.empresa_id == 1

    assert cuenta.nombre == "Caja Principal"

def test_modificar_no_modifica_cuenta_de_otra_empresa(
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
            nombre="Caja Empresa 1",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    cuenta_modificada = Cuenta(
        id=10,
        empresa_id=2,
        codigo="1.1.01",
        nombre="Caja Modificada Empresa 2",
        tipo=TipoCuenta.ACTIVO,
    )

    repository.modificar(
        empresa_id=2,
        cuenta=cuenta_modificada,
    )

    cuenta_empresa_1 = repository.buscar_por_id(
        empresa_id=1,
        cuenta_id=10,
    )

    cuenta_empresa_2 = repository.buscar_por_id(
        empresa_id=2,
        cuenta_id=10,
    )

    assert cuenta_empresa_1 is not None

    assert cuenta_empresa_1.nombre == (
        "Caja Empresa 1"
    )

    assert cuenta_empresa_2 is None
def test_eliminar_quita_la_cuenta_de_la_empresa(
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

    repository.eliminar(
        empresa_id=1,
        cuenta_id=10,
    )

    cuenta = repository.buscar_por_id(
        empresa_id=1,
        cuenta_id=10,
    )

    assert cuenta is None

def test_eliminar_no_quita_cuenta_de_otra_empresa(
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
            nombre="Caja Empresa 1",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    repository.guardar(
        Cuenta(
            id=10,
            empresa_id=2,
            codigo="1.1.01",
            nombre="Caja Empresa 2",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    repository.eliminar(
        empresa_id=1,
        cuenta_id=10,
    )

    cuenta_empresa_1 = repository.buscar_por_id(
        empresa_id=1,
        cuenta_id=10,
    )

    cuenta_empresa_2 = repository.buscar_por_id(
        empresa_id=2,
        cuenta_id=10,
    )

    assert cuenta_empresa_1 is None

    assert cuenta_empresa_2 is not None

    assert cuenta_empresa_2.nombre == (
        "Caja Empresa 2"
    )