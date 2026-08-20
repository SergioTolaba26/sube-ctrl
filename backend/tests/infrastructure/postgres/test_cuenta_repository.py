from dotenv import load_dotenv

load_dotenv()

from domain.entities.empresa import Empresa
from infrastructure.postgres.empresa_repository import EmpresaRepositoryPostgres
from infrastructure.postgres.database import (
    DatabasePostgres,
)

from infrastructure.postgres.cuenta_repository import (
    CuentaRepositoryPostgres,
)

from domain.entities.cuenta import Cuenta

from domain.enums.tipo_cuenta import TipoCuenta


def crear_repository():

    database = DatabasePostgres()

    return CuentaRepositoryPostgres(
        database.connection,
    )


def test_guardar_y_buscar_por_id():

    repository = crear_repository()

    cuenta = Cuenta(
        id=1001,
        empresa_id=1,
        codigo="9.1.01",
        nombre="Cuenta Test PostgreSQL",
        tipo=TipoCuenta.ACTIVO,
        activa=True,
        imputable=True,
    )

    repository.guardar(
        cuenta,
    )

    encontrada = repository.buscar_por_id(
        empresa_id=1,
        cuenta_id=1001,
    )

    assert encontrada is not None

    assert encontrada.id == 1001

    assert encontrada.empresa_id == 1

    assert encontrada.codigo == "9.1.01"

    assert encontrada.nombre == (
        "Cuenta Test PostgreSQL"
    )


def test_listar_filtra_por_empresa():

    repository = crear_repository()

    empresa_repository = EmpresaRepositoryPostgres(
        repository._connection,
    )

    empresa_repository.guardar(
        Empresa(
            id=1,
            razon_social="Empresa Test 1",
            nombre_fantasia="Empresa Test 1",
            cuit="30999999991",
        )
    )

    empresa_repository.guardar(
        Empresa(
            id=2,
            razon_social="Empresa Test 2",
            nombre_fantasia="Empresa Test 2",
            cuit="30999999992",
        )
    )

    repository.guardar(
        Cuenta(
            id=1002,
            empresa_id=1,
            codigo="9.1.02",
            nombre="Cuenta Empresa 1",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    repository.guardar(
        Cuenta(
            id=1003,
            empresa_id=2,
            codigo="9.1.02",
            nombre="Cuenta Empresa 2",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    cuentas_empresa_1 = repository.listar(
        empresa_id=1,
    )

    assert any(
        cuenta.id == 1002
        for cuenta in cuentas_empresa_1
    )

    assert all(
        cuenta.empresa_id == 1
        for cuenta in cuentas_empresa_1
    )

def test_buscar_por_id_no_devuelve_cuenta_de_otra_empresa():

    repository = crear_repository()

    repository.guardar(
        Cuenta(
            id=1004,
            empresa_id=1,
            codigo="9.1.04",
            nombre="Cuenta Empresa 1",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    cuenta = repository.buscar_por_id(
        empresa_id=2,
        cuenta_id=1004,
    )

    assert cuenta is None


def test_buscar_por_codigo():

    repository = crear_repository()

    repository.guardar(
        Cuenta(
            id=1005,
            empresa_id=1,
            codigo="9.1.05",
            nombre="Cuenta por Código",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    cuenta = repository.buscar_por_codigo(
        empresa_id=1,
        codigo="9.1.05",
    )

    assert cuenta is not None

    assert cuenta.id == 1005


def test_modificar():

    repository = crear_repository()

    repository.guardar(
        Cuenta(
            id=1006,
            empresa_id=1,
            codigo="9.1.06",
            nombre="Nombre Original",
            tipo=TipoCuenta.ACTIVO,
            activa=True,
            imputable=True,
        )
    )

    cuenta_modificada = Cuenta(
        id=1006,
        empresa_id=1,
        codigo="9.1.06",
        nombre="Nombre Modificado",
        tipo=TipoCuenta.ACTIVO,
        activa=True,
        imputable=False,
    )

    resultado = repository.modificar(
        empresa_id=1,
        cuenta=cuenta_modificada,
    )

    assert resultado is not None

    assert resultado.nombre == (
        "Nombre Modificado"
    )

    encontrada = repository.buscar_por_id(
        empresa_id=1,
        cuenta_id=1006,
    )

    assert encontrada is not None

    assert encontrada.nombre == (
        "Nombre Modificado"
    )

    assert encontrada.imputable is False


def test_modificar_no_modifica_cuenta_de_otra_empresa():

    repository = crear_repository()

    repository.guardar(
        Cuenta(
            id=1007,
            empresa_id=1,
            codigo="9.1.07",
            nombre="Cuenta Empresa 1",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    cuenta_modificada = Cuenta(
        id=1007,
        empresa_id=1,
        codigo="9.1.07",
        nombre="Intento Modificación",
        tipo=TipoCuenta.ACTIVO,
    )

    resultado = repository.modificar(
        empresa_id=2,
        cuenta=cuenta_modificada,
    )

    assert resultado is None

    cuenta = repository.buscar_por_id(
        empresa_id=1,
        cuenta_id=1007,
    )

    assert cuenta is not None

    assert cuenta.nombre == (
        "Cuenta Empresa 1"
    )


def test_eliminar():

    repository = crear_repository()

    repository.guardar(
        Cuenta(
            id=1008,
            empresa_id=1,
            codigo="9.1.08",
            nombre="Cuenta a Eliminar",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    eliminada = repository.eliminar(
        empresa_id=1,
        cuenta_id=1008,
    )

    assert eliminada is not None

    assert eliminada.id == 1008

    cuenta = repository.buscar_por_id(
        empresa_id=1,
        cuenta_id=1008,
    )

    assert cuenta is None


def test_eliminar_no_elimina_cuenta_de_otra_empresa():

    repository = crear_repository()

    repository.guardar(
        Cuenta(
            id=1009,
            empresa_id=1,
            codigo="9.1.09",
            nombre="Cuenta Protegida",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    eliminada = repository.eliminar(
        empresa_id=2,
        cuenta_id=1009,
    )

    assert eliminada is None

    cuenta = repository.buscar_por_id(
        empresa_id=1,
        cuenta_id=1009,
    )

    assert cuenta is not None