from pathlib import Path

from domain.entities.ejercicio_contable import (
    EjercicioContable,
)

from domain.repositories.ejercicio_repository import (
    EjercicioRepository,
)

from persistence.json_storage import (
    JsonStorage,
)


class EjercicioRepositoryJson(
    EjercicioRepository,
):

    def __init__(
        self,
        file_path: Path | None = None,
    ):

        if file_path is None:

            file_path = Path(
                "data/ejercicios.json"
            )

        self.storage = JsonStorage(
            file_path
        )

    def guardar(
        self,
        ejercicio: EjercicioContable,
    ) -> None:
        raise NotImplementedError

    def obtener_todos(
        self,
    ) -> list[EjercicioContable]:
        raise NotImplementedError

    def obtener_abierto(
        self,
    ) -> EjercicioContable | None:
        raise NotImplementedError

    def eliminar(
        self,
        ejercicio: EjercicioContable,
    ) -> None:
        raise NotImplementedError