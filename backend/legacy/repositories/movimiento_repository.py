from pathlib import Path

from domain.entities.movimiento import Movimiento
from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)

from persistence.repositories.base_repository_json import (
    BaseRepositoryJson,
)


class MovimientoRepositoryJson(
    BaseRepositoryJson,
    MovimientoRepository,
):

    def __init__(
        self,
        file_path: Path | None = None,
    ):

        if file_path is None:

            file_path = Path(
                "data/movimientos.json"
            )

        super().__init__(
            file_path,
            "movimientos",
        )

    def obtener_todos(
        self,
    ) -> list[Movimiento]:

        return super().obtener_todos()

    def buscar_por_id(
        self,
        movimiento_id: int,
    ) -> Movimiento | None:

        raise NotImplementedError

    def _to_dict(
        self,
        movimiento: Movimiento,
    ) -> dict:

        raise NotImplementedError

    def _from_dict(
        self,
        data: dict,
    ) -> Movimiento:

        raise NotImplementedError