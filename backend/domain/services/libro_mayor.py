from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento

from decimal import Decimal

from domain.value_objects.renglon_libro_mayor import RenglonLibroMayor


class LibroMayor:

    def obtener(self, cuenta, movimientos):

        lineas = []

        for movimiento in movimientos:


            if not movimiento.esta_confirmado():
                continue

            for linea in movimiento.lineas:
                # print(
                # linea.cuenta.nombre,
                # linea.cuenta is cuenta,
                # linea.cuenta == cuenta,
                #  )

                if linea.cuenta == cuenta:
                    lineas.append(linea)

        lineas.sort(
            key=lambda linea: linea.movimiento.fecha
        )

        saldo = Decimal("0")

        renglones = []

        for linea in lineas:

            saldo = cuenta.aplicar_afectacion(
                saldo_actual=saldo,
                tipo_afectacion=linea.tipo_afectacion,
                importe=linea.importe,
            )

            renglones.append(
                RenglonLibroMayor(
                    linea=linea,
                    saldo=saldo,
                )
            )
        # print(
        # cuenta.nombre,
        # len(renglones),
        # )
        return renglones
            

    
