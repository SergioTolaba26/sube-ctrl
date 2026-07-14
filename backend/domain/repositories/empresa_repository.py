from abc import ABC
from abc import abstractmethod

from domain.entities.empresa import Empresa


class EmpresaRepository(ABC):
    """
    Contrato para la persistencia de empresas.
    El dominio depende únicamente de esta interfaz.
    """

    @abstractmethod
    def guardar(
        self,
        empresa: Empresa,
    ) -> None:
        """
        Persiste una empresa.
        """
        raise NotImplementedError

    @abstractmethod
    def obtener_todas(
        self,
    ) -> list[Empresa]:
        """
        Devuelve todas las empresas.
        """
        raise NotImplementedError

    @abstractmethod
    def buscar_por_cuit(
        self,
        cuit: str,
    ) -> Empresa | None:
        """
        Busca una empresa por CUIT.
        """
        raise NotImplementedError

    @abstractmethod
    def eliminar(
        self,
        empresa: Empresa,
    ) -> None:
        """
        Elimina una empresa.
        """
        raise NotImplementedError