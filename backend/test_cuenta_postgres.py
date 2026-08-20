from dotenv import load_dotenv

load_dotenv()

from infrastructure.postgres.database import (
    DatabasePostgres,
)

from infrastructure.postgres.cuenta_repository import (
    CuentaRepositoryPostgres,
)

from domain.entities.cuenta import Cuenta

from domain.enums.tipo_cuenta import TipoCuenta


database = DatabasePostgres()

repository = CuentaRepositoryPostgres(
    database.connection,
)


cuenta = Cuenta(
    id=1,
    empresa_id=1,
    codigo="1.1.01",
    nombre="Caja PostgreSQL",
    tipo=TipoCuenta.ACTIVO,
    activa=True,
    imputable=True,
)


repository.guardar(
    cuenta,
)


print(
    "GUARDADA:",
    cuenta,
)


cuentas = repository.listar(
    empresa_id=1,
)


print(
    "LISTADAS:",
    cuentas,
)


encontrada = repository.buscar_por_id(
    empresa_id=1,
    cuenta_id=1,
)


print(
    "BUSCADA:",
    encontrada,
)


por_codigo = repository.buscar_por_codigo(
    empresa_id=1,
    codigo="1.1.01",
)


print(
    "POR CODIGO:",
    por_codigo,
)