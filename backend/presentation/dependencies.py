from infrastructure.postgres.database import (
    DatabasePostgres,
)

from infrastructure.postgres.empresa_repository import (
    EmpresaRepositoryPostgres,
)

from infrastructure.postgres.cuenta_repository import (
    CuentaRepositoryPostgres,
)


def get_empresa_repository():

    database = DatabasePostgres()

    return EmpresaRepositoryPostgres(
        database.connection,
    )


def get_cuenta_repository():

    database = DatabasePostgres()

    return CuentaRepositoryPostgres(
        database.connection,
    )