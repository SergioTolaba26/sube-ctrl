from abc import ABC, abstractmethod

from domain.enums.estado_ejercicio import EstadoEjercicio
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
    def obtener_todos(
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
    ):

        for ejercicio in self.listar():

            if (
                ejercicio.empresa_id == empresa_id
                and
                ejercicio.anio == anio
            ):
                return ejercicio

        return None

    @abstractmethod
    def buscar_abierto(
        self,
        empresa_id: int,
    ):

        for ejercicio in self.listar():

            if (
                ejercicio.empresa_id == empresa_id
                and
                ejercicio.estado == EstadoEjercicio.ABIERTO
            ):
                return ejercicio

        return None

    @abstractmethod
    def obtener_abierto(
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

    def obtener_todos(
        self,
    ):
        return self.listar()
    
    def obtener_abierto(
        self,
        empresa_id: int,
    ):
        for ejercicio in self.listar():

            if (
                ejercicio.empresa_id == empresa_id
                and
                ejercicio.estado == EstadoEjercicio.ABIERTO
            ):
                return ejercicio

        return None