from pathlib import Path

from persistence.json_storage import JsonStorage

from infrastructure.repositories.json.cuenta_repository import (
    CuentaRepositoryJson,
)

from domain.services.cuenta_service import (
    CuentaService,
)

from application.use_cases.cuenta.registrar_cuenta import (
    RegistrarCuenta,
)


def crear_registrar_cuenta():

    storage = JsonStorage(
        Path("data/cuentas.json"),
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    service = CuentaService(
        repository,
    )

    return RegistrarCuenta(
        service,
    )