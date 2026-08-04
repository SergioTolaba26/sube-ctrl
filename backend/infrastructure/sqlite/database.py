import sqlite3

from infrastructure.config.settings import DATABASE_PATH
from infrastructure.sqlite.schema import SCHEMA

class Database:
    """
    Administra la conexión SQLite del ERP.
    """

    def __init__(self):

        DATABASE_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self._connection = sqlite3.connect(
            DATABASE_PATH,
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