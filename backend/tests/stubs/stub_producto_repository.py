from domain.entities.producto import Producto


class StubProductoRepository:

    def __init__(self):

        self._productos = []
        self._siguiente_id = 1

    def guardar(
        self,
        producto: Producto,
    ) -> Producto:

        producto.id = self._siguiente_id

        self._siguiente_id += 1

        self._productos.append(
            producto,
        )

        return producto

    def buscar_por_id(
        self,
        empresa_id: int,
        producto_id: int,
    ) -> Producto | None:

        for producto in self._productos:

            if (
                producto.id == producto_id
                and producto.empresa_id == empresa_id
            ):
                return producto

        return None

    def buscar_por_codigo_barras(
        self,
        empresa_id: int,
        codigo_barras: str,
    ) -> Producto | None:

        for producto in self._productos:

            if (
                producto.empresa_id == empresa_id
                and producto.codigo_barras == codigo_barras
            ):
                return producto

        return None

    def obtener_todos(
        self,
        empresa_id: int,
    ) -> list[Producto]:

        return [
            producto
            for producto in self._productos
            if producto.empresa_id == empresa_id
        ]

    def modificar(
        self,
        producto: Producto,
    ) -> Producto | None:

        for indice, existente in enumerate(
            self._productos,
        ):

            if (
                existente.id == producto.id
                and existente.empresa_id == producto.empresa_id
            ):
                self._productos[indice] = producto

                return producto

        return None

    def eliminar(
        self,
        empresa_id: int,
        producto_id: int,
    ) -> bool:

        for indice, producto in enumerate(
            self._productos,
        ):

            if (
                producto.id == producto_id
                and producto.empresa_id == empresa_id
            ):
                del self._productos[indice]

                return True

        return False