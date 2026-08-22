import os

import psycopg

from dotenv import load_dotenv


load_dotenv()


class DatabasePostgres:

    def __init__(
        self,
    ):

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

    def close(
        self,
    ):

        if (
            self.connection
            and not self.connection.closed
        ):

            self.connection.close()