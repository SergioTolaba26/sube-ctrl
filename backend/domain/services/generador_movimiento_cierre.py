from decimal import Decimal

from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta
from domain.value_objects.resultado_ejercicio import ResultadoEjercicio


class GeneradorMovimientoCierre:

    def generar(
        self,
        ejercicio,
        saldos,
    ):
        movimiento = Movimiento(
            id=None,
            empresa_id=ejercicio.empresa_id,
            ejercicio_id=ejercicio.id,
            fecha=ejercicio.fecha_fin,
            descripcion="Cierre del ejercicio",
        )

        resultado = Decimal("0")

        for saldo in saldos:

            movimiento.agregar_linea(
                saldo.generar_linea_de_cierre()
            )

            if saldo.cuenta.tipo == TipoCuenta.INGRESO:
                resultado += saldo.saldo
            else:
                resultado -= saldo.saldo

        movimiento.agregar_linea(
            ResultadoEjercicio(
                importe=resultado,
            ).generar_linea_de_cierre()
        )

        return movimiento