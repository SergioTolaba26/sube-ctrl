from abc import ABC, abstractmethod

from domain.entities.ejercicio import Ejercicio

class EjercicioRepository(ABC):


    @abstractmethod
    def guardar(
        self,
        ejercicio: Ejercicio,
    ) -> None:
        pass

    @abstractmethod
    def listar(
        self,
    ) -> list[Ejercicio]:
        pass

    @abstractmethod
    def buscar_por_id(
        self,
        ejercicio_id: int,
    ) -> Ejercicio | None:
        pass

    @abstractmethod
    def buscar_por_anio(
        self,
        empresa_id: int,
        anio: int,
    ) -> Ejercicio | None:
        pass

    @abstractmethod
    def buscar_abierto(
        self,
        empresa_id: int,
    ) -> Ejercicio | None:
        pass

    @abstractmethod
    def eliminar(
        self,
        id_: int,
    ) -> None:
        pass

    @abstractmethod
    def actualizar(
        self,
        ejercicio: Ejercicio,
    ) -> None:
        pass

