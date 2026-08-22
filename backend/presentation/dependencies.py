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
from application.factory import (
    ApplicationFactory,
)

def get_empresa_repository():

    database = DatabasePostgres()

    try:

        yield EmpresaRepositoryPostgres(
            database.connection,
        )

    finally:

        database.connection.close()


def get_cuenta_repository():

    database = DatabasePostgres()

    try:

        yield CuentaRepositoryPostgres(
            database.connection,
        )

    finally:

        database.connection.close()


def get_producto_repository():

    database = DatabasePostgres()

    try:

        yield ProductoRepositoryPostgres(
            database.connection,
        )

    finally:

        database.connection.close()

def get_application_factory():

    database = DatabasePostgres()

    try:

        yield ApplicationFactory(
            database.connection,
        )

    finally:

        database.connection.close()