from domain.entities.movimiento import Movimiento
from domain.entities.linea_movimiento import LineaMovimiento
from domain.enums.estado_movimiento import EstadoMovimiento
from domain.enums.tipo_afectacion import TipoAfectacion


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
            empresa_id=ejercicio.empresa_id,
            ejercicio_id=ejercicio.id,
            fecha=fecha,
            descripcion=descripcion,
            estado=EstadoMovimiento.BORRADOR,
            lineas=[],
        )

        for dato in lineas:

            cuenta = self.cuenta_service.buscar_por_id(
                dato["cuenta_id"],
            )

            if cuenta is None:
                raise ValueError(
                    f"No existe la cuenta {dato['cuenta_id']}"
                )

            if dato["tipo_afectacion"] == TipoAfectacion.DEBITO:
                linea = LineaMovimiento.debito(
                    cuenta,
                    dato["importe"],
                )
            else:
                linea = LineaMovimiento.credito(
                    cuenta,
                    dato["importe"],
                )

            movimiento.agregar_linea(
                linea,
            )

        self.movimiento_service.guardar(
            movimiento,
        )

        return movimiento