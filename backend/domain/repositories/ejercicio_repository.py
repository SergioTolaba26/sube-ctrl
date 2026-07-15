from abc import ABC, abstractmethod

from domain.entities.ejercicio_contable import (
    EjercicioContable,
)


class EjercicioRepository(ABC):

    @abstractmethod
    def guardar(
        self,
        ejercicio: EjercicioContable,
    ) -> None:
        pass

    @abstractmethod
    def obtener_todos(
        self,
    ) -> list[EjercicioContable]:
        pass

    @abstractmethod
    def obtener_abierto(
        self,
    ) -> EjercicioContable | None:
        pass

    @abstractmethod
    def eliminar(
        self,
        ejercicio: EjercicioContable,
    ) -> None:
        pass