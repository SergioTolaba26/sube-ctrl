from datetime import date
from pathlib import Path

from domain.entities.ejercicio_contable import (
    EjercicioContable,
)
from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)
from domain.repositories.ejercicio_repository import (
    EjercicioRepository,
)

from persistence.repositories.base_repository_json import (
    BaseRepositoryJson,
)


class EjercicioRepositoryJson(
    BaseRepositoryJson,
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

        super().__init__(
            file_path,
            "ejercicios",
        )

    def obtener_abierto(
        self,
    ) -> EjercicioContable | None:

        for ejercicio in self.obtener_todos():

            if ejercicio.esta_abierto():

                return ejercicio

        return None

    def _to_dict(
        self,
        ejercicio: EjercicioContable,
    ) -> dict:

        return {

            "id": ejercicio.id,

            "empresa_id": ejercicio.empresa_id,

            "fecha_inicio": ejercicio.fecha_inicio.isoformat(),

            "fecha_fin": ejercicio.fecha_fin.isoformat(),

            "estado": ejercicio.estado.name,

        }

    def _from_dict(
        self,
        data: dict,
    ) -> EjercicioContable:

        return EjercicioContable(

            id=data["id"],

            empresa_id=data["empresa_id"],

            fecha_inicio=date.fromisoformat(
                data["fecha_inicio"]
            ),

            fecha_fin=date.fromisoformat(
                data["fecha_fin"]
            ),

            estado=EstadoEjercicio[
                data["estado"]
            ],

        )