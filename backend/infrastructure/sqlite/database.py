import sqlite3
from infrastructure.config.settings import DATABASE_PATH
from infrastructure.sqlite.schema import SCHEMA
from pathlib import Path

class Database:
    """
    Administra la conexión SQLite del ERP.
    """

    def __init__(
        self,
        database_path=None,
    ):
        database_path = Path(database_path)

        database_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        if database_path is None:
            database_path = DATABASE_PATH
        self._connection = sqlite3.connect(
            database_path ,
        )

        self._connection.row_factory = sqlite3.Row

    @property
    def connection(self):
        return self._connection
    
    def crear_tablas(
        self,
    ) -> None:
        """
        Crea todas las tablas definidas
        en infrastructure.sqlite.schema.
        """

        cursor = self._connection.cursor()

        for sentencia in SCHEMA:

            cursor.execute(
                sentencia,
            )

        self._connection.commit()

    def close(self):
        self._connection.close()