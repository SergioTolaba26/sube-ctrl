class BaseRepository:
    """
    Repositorio base para implementaciones SQLite.
    Centraliza el acceso a la conexión.
    """

    def __init__(
        self,
        connection,
    ):
        self._connection = connection