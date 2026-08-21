from infrastructure.postgres.database import (
    DatabasePostgres,
)

from infrastructure.postgres.empresa_repository import (
    EmpresaRepositoryPostgres,
)

from infrastructure.postgres.cuenta_repository import (
    CuentaRepositoryPostgres,
)

from infrastructure.postgres.producto_repository import (
    ProductoRepositoryPostgres,
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


def get_producto_repository():

    database = DatabasePostgres()

    return ProductoRepositoryPostgres(
        database.connection,
    )