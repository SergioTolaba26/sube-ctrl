from abc import (
    ABC,
    abstractmethod,
)

from domain.entities.cuenta import Cuenta


class PlanCuentaRepository(
    ABC,
):

    @abstractmethod
    def guardar(
        self,
        cuenta: Cuenta,
    ) -> None:
        pass

    @abstractmethod
    def obtener_todas(
        self,
    ) -> list[Cuenta]:
        pass

    @abstractmethod
    def buscar_por_codigo(
        self,
        codigo: str,
    ) -> Cuenta | None:
        pass

    @abstractmethod
    def eliminar(
        self,
        cuenta: Cuenta,
    ) -> None:
        pass