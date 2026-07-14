from domain.enums.tipo_cuenta import TipoCuenta
from domain.use_cases.cerrar_ejercicio import (
    CerrarEjercicio,
)

from domain.entities.movimiento import Movimiento

from tests.builders.entidades_builder import (
    crear_ejercicio,
)

from tests.builders.movimientos_builder import (
    crear_movimientos_del_ejercicio,
)


# def test_genera_un_movimiento_de_cierre():

#     proceso = CerrarEjercicio()

#     movimientos = crear_movimientos_del_ejercicio()

#     movimiento = proceso.ejecutar(
#         ejercicio=crear_ejercicio(),
#         movimientos=movimientos,
#     )

#     assert isinstance(
#         movimiento,
#         Movimiento,
#     )


# def test_el_movimiento_de_cierre_queda_confirmado():

#     caso = CerrarEjercicio()

#     movimientos = crear_movimientos_del_ejercicio()

#     movimiento = caso.ejecutar(
#         ejercicio=crear_ejercicio(),
#         movimientos=movimientos,
#     )

#     assert movimiento.esta_confirmado()


# def test_el_movimiento_de_cierre_genera_lineas():

#     caso = CerrarEjercicio()

#     movimientos = crear_movimientos_del_ejercicio()

#     movimiento = caso.ejecutar(
#         ejercicio=crear_ejercicio(),
#         movimientos=movimientos,
#     )

#     assert len(movimiento.lineas) > 0

# def test_el_cierre_genera_una_linea_por_cada_cuenta_de_resultado():

#     caso = CerrarEjercicio()

#     movimientos = crear_movimientos_del_ejercicio()

#     movimiento = caso.ejecutar(
#         ejercicio=crear_ejercicio(),
#         movimientos=movimientos,
#     )

#     cuentas_resultado = {
#         linea.cuenta.codigo
#         for movimiento_original in movimientos
#         for linea in movimiento_original.lineas
#         if linea.cuenta.tipo in (
#             TipoCuenta.INGRESO,
#             TipoCuenta.GASTO,
#         )
#     }

#     assert len(movimiento.lineas) == len(cuentas_resultado)