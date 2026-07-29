from abc import (
    ABC,
    abstractmethod,
)

from domain.entities.movimiento import (
    Movimiento,
)


class MovimientoRepository(
    ABC,
):

    @abstractmethod
    def listar(
        self,
    ) -> list[Movimiento]:
        pass

    @abstractmethod
    def listar_por_fecha(
        self,
        desde,
        hasta,
    ) -> list[Movimiento]:
        pass

    @abstractmethod
    def guardar(
        self,
        movimiento: Movimiento,
    ) -> None:
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
        movimiento_id: int,
    ) -> None:
        pass