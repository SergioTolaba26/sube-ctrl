from infrastructure.persistence.base.storage import (
    Storage,
)

from infrastructure.repositories.json.movimiento_repository import (
    MovimientoRepositoryJson,
)


class FakeCuentaRepository:
    pass


def test_crea_repositorio(
    tmp_path,
):

    storage = Storage(
        tmp_path / "movimientos.json",
    )

    repository = MovimientoRepositoryJson(
        storage,
        FakeCuentaRepository(),
    )

    assert repository.storage is storage

    assert repository.cuenta_repository is not None