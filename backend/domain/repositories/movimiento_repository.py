from abc import (
    ABC,
    abstractmethod,
)

from domain.entities.movimiento import Movimiento


class MovimientoRepository(
    ABC,
):

    @abstractmethod
    def guardar(
        self,
        movimiento: Movimiento,
    ) -> None:
        pass

    @abstractmethod
    def obtener_todos(
        self,
    ) -> list[Movimiento]:
        pass

    @abstractmethod
    def buscar_por_id(
        self,
        movimiento_id: int,
    ) -> Movimiento | None:
        pass

    @abstractmethod
    def eliminar(
        self,
        movimiento: Movimiento,
    ) -> None:
        pass