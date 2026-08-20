import os

import psycopg


class DatabasePostgres:

    def __init__(self):

        database_url = os.getenv(
            "DATABASE_URL",
        )

        if not database_url:
            raise RuntimeError(
                "DATABASE_URL no está configurada."
            )

        self.connection = psycopg.connect(
            database_url,
        )