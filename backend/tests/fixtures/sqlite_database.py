from pathlib import Path

import pytest

from infrastructure.sqlite.database import Database


TEST_DATABASE_PATH = Path("data/test_erp.db")


@pytest.fixture
def database():

    if TEST_DATABASE_PATH .exists():
        TEST_DATABASE_PATH.unlink()

    db = Database(
        TEST_DATABASE_PATH,
    )

    db.crear_tablas()

    yield db

    db.close()

    if TEST_DATABASE_PATH.exists():
       TEST_DATABASE_PATH.unlink()