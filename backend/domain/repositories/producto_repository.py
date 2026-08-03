from abc import ABC, abstractmethod

from domain.entities.producto import Producto


class ProductoRepository(ABC):
    """
    Contrato para la persistencia de productos.
    """

    @abstractmethod
    def guardar(
        self,
        producto: Producto,
    ) -> Producto:
        """
        Guarda un producto.
        """
        pass

    @abstractmethod
    def obtener_por_id(
        self,
        producto_id: int,
    ) -> Producto | None:
        """
        Obtiene un producto por su ID.
        """
        pass

    @abstractmethod
    def obtener_por_codigo_barras(
        self,
        codigo_barras: str,
    ) -> Producto | None:
        """
        Obtiene un producto por código de barras.
        """
        pass

    @abstractmethod
    def listar(self) -> list[Producto]:
        """
        Devuelve todos los productos.
        """
        pass

    @abstractmethod
    def actualizar(
        self,
        producto: Producto,
    ) -> Producto:
        """
        Actualiza un producto.
        """
        pass

    @abstractmethod
    def eliminar(
        self,
        producto_id: int,
    ) -> None:
        """
        Elimina un producto.
        """
        pass