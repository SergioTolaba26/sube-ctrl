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
from datetime import date

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
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

    # def guardar(
    #     self,
    #     ejercicio: EjercicioContable,
    # ) -> None:
    #     raise 
    
    def guardar(
        self,
        ejercicio: EjercicioContable,
    ) -> None:

        ejercicios = self.storage.read_list(
            "ejercicios"
        )

        ejercicios.append(
            self._to_dict(
                ejercicio
            )
        )

        self.storage.write_list(
            "ejercicios",
            ejercicios,
        )

    # def obtener_todos(
    #     self,
    # ) -> list[EjercicioContable]:
    #     raise NotImplementedError
    def obtener_todos(
        self,
    ) -> list[EjercicioContable]:

        ejercicios = self.storage.read_list(
            "ejercicios"
        )

        return [

            self._from_dict(data)

            for data in ejercicios
        ]

    # def obtener_abierto(
    #     self,
    # ) -> EjercicioContable | None:
    #     raise 
    
    def obtener_abierto(
        self,
    ) -> EjercicioContable | None:

        for ejercicio in self.obtener_todos():

            if ejercicio.esta_abierto():

                return ejercicio

        return None

    # def eliminar(
    #     self,
    #     ejercicio: EjercicioContable,
    # ) -> None:
    #     raise NotImplementedError
    def eliminar(
        self,
        ejercicio: EjercicioContable,
    ) -> None:

        ejercicios = self.storage.read_list(
            "ejercicios"
        )

        ejercicios = [

            data

            for data in ejercicios

            if data["id"] != ejercicio.id

        ]

        self.storage.write_list(
            "ejercicios",
            ejercicios,
        )
    
    def _to_dict(
        self,
        ejercicio: EjercicioContable,
    ) -> dict:

        return {

            "id": ejercicio.id,

            "empresa_id": ejercicio.empresa_id,

            "fecha_inicio":
                ejercicio.fecha_inicio.isoformat(),

            "fecha_fin":
                ejercicio.fecha_fin.isoformat(),

            "estado":
                ejercicio.estado.name,
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
    
