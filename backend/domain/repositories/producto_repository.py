from abc import ABC
from abc import abstractmethod

from domain.entities.producto import Producto


class ProductoRepository(ABC):
    """
    Contrato para la persistencia de productos.

    El dominio depende únicamente de esta interfaz.
    """

    @abstractmethod
    def guardar(
        self,
        producto: Producto,
    ) -> None:
        """
        Persiste un producto.
        """
        raise NotImplementedError

    @abstractmethod
    def obtener_todos(
        self,
    ) -> list[Producto]:
        """
        Devuelve todos los productos.
        """
        raise NotImplementedError

    @abstractmethod
    def buscar_por_id(
        self,
        id_: int,
    ) -> Producto | None:
        """
        Busca un producto por su identificador.
        """
        raise NotImplementedError

    @abstractmethod
    def buscar_por_codigo_barras(
        self,
        codigo_barras: str,
    ) -> Producto | None:
        """
        Busca un producto por su código de barras.
        """
        raise NotImplementedError

    @abstractmethod
    def eliminar(
        self,
        producto: Producto,
    ) -> None:
        """
        Elimina un producto.
        """
        raise NotImplementedError