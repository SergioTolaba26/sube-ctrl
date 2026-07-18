from datetime import date

from domain.entities.ejercicio_contable import (
    EjercicioContable,
)
from domain.repositories.ejercicio_repository import (
    EjercicioRepository,
)


class RegistrarEjercicio:

    def __init__(
        self,
        repository: EjercicioRepository,
    ):
        self.repository = repository

    def execute(
        self,
        empresa_id: int,
        fecha_inicio: str,
        fecha_fin: str,
    ):

        ejercicio = EjercicioContable(
            id=None,
            empresa_id=empresa_id,
            fecha_inicio=date.fromisoformat(
                fecha_inicio
            ),
            fecha_fin=date.fromisoformat(
                fecha_fin
            ),
        )

        self.repository.guardar(
            ejercicio
        )

        return ejercicio