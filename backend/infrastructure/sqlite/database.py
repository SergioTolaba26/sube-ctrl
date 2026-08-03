import sqlite3
from pathlib import Path


class Database:
    """
    Administra la conexión SQLite del ERP.
    """

    def __init__(
        self,
        db_name: str = "erp.db",
    ):

        self._db_path = (
            Path(__file__).parent / db_name
        )

        self._connection = sqlite3.connect(
            self._db_path,
        )

        self._connection.row_factory = (
            sqlite3.Row
        )

    @property
    def connection(
        self,
    ):
        return self._connection

    def close(
        self,
    ):

        self._connection.close()