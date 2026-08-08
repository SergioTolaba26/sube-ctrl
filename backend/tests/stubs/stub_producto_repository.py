from domain.entities.producto import Producto
from domain.repositories.producto_repository import (
    ProductoRepository,
)


class StubProductoRepository(
    ProductoRepository,
):

    def __init__(self):

        self._productos: list[Producto] = []
        self._ultimo_id = 0

    def guardar(
        self,
        producto: Producto,
    ) -> Producto:

        self._ultimo_id += 1

        producto.id = self._ultimo_id

        self._productos.append(
            producto,
        )

        return producto

    def buscar_por_id(
        self,
        producto_id: int,
    ) -> Producto | None:

        for producto in self._productos:

            if producto.id == producto_id:
                return producto

        return None

    def buscar_por_codigo_barras(
        self,
        codigo_barras: str,
    ) -> Producto | None:

        for producto in self._productos:

            if (
                producto.codigo_barras
                == codigo_barras
            ):
                return producto

        return None

    def obtener_todos(
        self,
    ) -> list[Producto]:

        return self._productos.copy()
    def actualizar(
        self,
        producto: Producto,
    ) -> Producto:

        for indice, existente in enumerate(
            self._productos,
        ):

            if existente.id == producto.id:

                self._productos[indice] = producto

                return producto

        raise ValueError(
            "Producto inexistente.",
        )


    def eliminar(
        self,
        producto_id: int,
    ) -> None:

        self._productos = [
            existente
            for existente in self._productos
            if existente.id != producto_id
        ]