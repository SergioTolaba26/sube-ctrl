from datetime import date
from decimal import Decimal

from domain.entities.cuenta import Cuenta

from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta



def crear_ventas():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="4.1.01",
        nombre="Ventas",
        tipo=TipoCuenta.INGRESO,
    )


def crear_sueldos():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="5.1.01",
        nombre="Sueldos",
        tipo=TipoCuenta.GASTO,
    )

# Se habilitará cuando el asiento de cierre genere
# las líneas contables correspondientes.
# def test_el_movimiento_de_cierre_contiene_las_cuentas_de_resultado():
#     """
#     El movimiento de cierre contiene
#     las cuentas de ingresos y gastos.
#     """

#     ejercicio = EjercicioContable(
#         id=None,
#         fecha_inicio=date(2026, 1, 1),
#         fecha_fin=date(2026, 12, 31),
#     )

#     ventas = crear_ventas()
#     sueldos = crear_sueldos()

#     movimiento = Movimiento(
#         id=None,
#         fecha=date(2026, 6, 1),
#         descripcion="Operación",
#     )

#     movimiento.agregar_linea(
#         LineaMovimiento.credito(
#             cuenta=ventas,
#             importe=Decimal("1000"),
#         )
#     )

#     movimiento.agregar_linea(
#         LineaMovimiento.debito(
#             cuenta=sueldos,
#             importe=Decimal("600"),
#         )
#     )

#     movimiento.confirmar()

#     cierre = CierreEjercicio()

#     movimiento_cierre = cierre.cerrar(
#         ejercicio,
#         movimientos=[movimiento],
#     )

#     cuentas = {
#         linea.cuenta.codigo
#         for linea in movimiento_cierre.lineas
#     }

#     assert ventas.codigo in cuentas
#     assert sueldos.codigo in cuentas

#*******************************Prox test tambien lo comento

# def test_el_movimiento_de_cierre_contiene_una_primera_linea():
#     """
#     El movimiento de cierre comienza a construir
#     el asiento agregando su primera línea.
#     """

#     ejercicio = EjercicioContable(
#         id=None,
#         fecha_inicio=date(2026, 1, 1),
#         fecha_fin=date(2026, 12, 31),
#     )

#     cierre = CierreEjercicio()

#     movimiento = cierre.cerrar(
#         ejercicio,
#         movimientos=[],
#     )

#     assert len(movimiento.lineas) == 1

