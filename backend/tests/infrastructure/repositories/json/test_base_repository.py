from infrastructure.persistence.base.storage import Storage
from infrastructure.mappers.cuenta_mapper import CuentaMapper
from infrastructure.repositories.json.base_repository import (
    BaseRepositoryJson,
)


def test_crea_base_repository(
    tmp_path,
):

    storage = Storage(
        tmp_path / "datos.json",
    )

    repository = BaseRepositoryJson(
        storage,
        CuentaMapper,
    )

    assert repository.storage is storage

    assert repository.mapper is CuentaMapper

