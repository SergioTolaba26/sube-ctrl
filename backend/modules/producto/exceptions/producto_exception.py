"""
Excepciones del módulo Producto.

Todas las excepciones específicas del módulo deberán heredar de
ProductoException.
"""


class ProductoException(Exception):
    """
    Excepción base del módulo Producto.
    """


class ProductoInvalidoError(ProductoException):
    """
    Se produce cuando un producto viola
    alguna regla del dominio.
    """