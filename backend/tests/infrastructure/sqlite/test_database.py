from tests.fixtures.sqlite_database import database


def test_database_fixture(
    database,
):
    assert database.connection is not None