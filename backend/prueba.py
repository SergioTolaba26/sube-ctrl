from tests.builders.movimientos_builder import (
    crear_movimientos_del_ejercicio,
)

movimientos = crear_movimientos_del_ejercicio()

print(len(movimientos))