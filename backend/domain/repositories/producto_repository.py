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
    ) -> Producto:
        """
        Persiste un producto.
        """
        raise NotImplementedError

    @abstractmethod
    def listar(
        self,
        empresa_id: int,
    ) -> list[Producto]:
        """
        Devuelve todos los productos de una empresa.
        """
        raise NotImplementedError

    @abstractmethod
    def buscar_por_id(
        self,
        empresa_id: int,
        producto_id: int,
    ) -> Producto | None:
        """
        Busca un producto por empresa e identificador.
        """
        raise NotImplementedError

    @abstractmethod
    def buscar_por_codigo_barras(
        self,
        empresa_id: int,
        codigo_barras: str,
    ) -> Producto | None:
        """
        Busca un producto por empresa y código de barras.
        """
        raise NotImplementedError

    @abstractmethod
    def modificar(
        self,
        producto: Producto,
    ) -> Producto | None:
        """
        Modifica un producto existente.
        """
        raise NotImplementedError

    @abstractmethod
    def eliminar(
        self,
        empresa_id: int,
        producto_id: int,
    ) -> bool:
        """
        Elimina un producto de una empresa.

        Devuelve True si el producto fue eliminado.
        """
        raise NotImplementedError