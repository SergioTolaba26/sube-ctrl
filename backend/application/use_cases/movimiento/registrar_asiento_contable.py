from domain.entities.movimiento import Movimiento
from domain.entities.linea_movimiento import LineaMovimiento
from domain.enums.estado_movimiento import EstadoMovimiento


class RegistrarAsientoContable:

    def __init__(
        self,
        movimiento_service,
        cuenta_service,
        ejercicio_service,
    ):
        self.movimiento_service = movimiento_service
        self.cuenta_service = cuenta_service
        self.ejercicio_service = ejercicio_service

    def execute(
        self,
        fecha,
        descripcion,
        lineas,
    ) -> Movimiento:

        ejercicio = self.ejercicio_service.buscar_por_fecha(
            fecha,
        )

        if ejercicio is None:

            raise ValueError(
                "No existe un ejercicio para la fecha indicada."
            )

        if ejercicio.esta_cerrado():

            raise ValueError(
                "No se puede registrar un asiento en un ejercicio cerrado."
            )

        movimiento = Movimiento(
            id=None,
            fecha=fecha,
            descripcion=descripcion,
            estado=EstadoMovimiento.BORRADOR,
            lineas=[],
        )

        for dato in lineas:

            cuenta = self.cuenta_service.buscar_por_id(
                dato["cuenta_id"],
            )

            if dato["debito"] > 0:

                linea = LineaMovimiento.debito(
                    cuenta,
                    dato["debito"],
                )

            else:

                linea = LineaMovimiento.credito(
                    cuenta,
                    dato["credito"],
                )

            movimiento.agregar_linea(
                linea,
            )

        #movimiento.confirmar() Lo elimino para que el asiento nazca como BORRADOR
        #
        # Verificación temporal
        #
        print("Cantidad de líneas:", len(movimiento.lineas))

        for linea in movimiento.lineas:
            print(
                linea.cuenta.id,
                linea.tipo_afectacion,
                linea.importe,
            )
            
        self.movimiento_service.guardar(
            movimiento,
        )

        return movimiento