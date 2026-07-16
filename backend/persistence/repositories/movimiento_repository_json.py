from pathlib import Path

from domain.entities.movimiento import Movimiento
from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)

from persistence.repositories.base_repository_json import (
    BaseRepositoryJson,
)


from pathlib import Path

from domain.repositories.plan_cuenta_repository import (
    PlanCuentaRepository,
)
from datetime import date

from domain.enums.estado_movimiento import (
    EstadoMovimiento,
)
from decimal import Decimal

from domain.entities.linea_movimiento import (
    LineaMovimiento,
)

from domain.enums.tipo_afectacion import (
    TipoAfectacion,
)


class MovimientoRepositoryJson(
    BaseRepositoryJson,
    MovimientoRepository,
):

    def __init__(
        self,
        plan_cuenta_repository: PlanCuentaRepository | None = None,
        file_path: Path | None = None,
    ):

        if file_path is None:

            file_path = Path(
                "data/movimientos.json"
            )

        super().__init__(
            file_path,
            "movimientos",
        )

        self.plan_cuenta_repository = (
            plan_cuenta_repository
        )
    def obtener_todos(
        self,
    ) -> list[Movimiento]:

        return super().obtener_todos()

    def buscar_por_id(
        self,
        movimiento_id: int,
    ) -> Movimiento | None:

        raise NotImplementedError

    # def _to_dict(
    #     self,
    #     movimiento: Movimiento,
    # ) -> dict:

    #     raise NotImplementedError
    def _to_dict(
        self,
        movimiento: Movimiento,
    ) -> dict:

        return {

            "id": movimiento.id,

            "estado": movimiento.estado.value,

            "fecha": movimiento.fecha.isoformat(),

            "descripcion": movimiento.descripcion,

            "lineas": [

                {

                    "codigo_cuenta": linea.cuenta.codigo,

                    "importe": str(
                        linea.importe
                    ),

                    "tipo_afectacion": (
                        linea.tipo_afectacion.value
                    ),

                }

                for linea in movimiento.lineas

            ],

        }
    # def _from_dict(
    #     self,
    #     data: dict,
    # ) -> Movimiento:

    #     raise NotImplementedError

    # def _from_dict(
    #     self,
    #     data: dict,
    # ) -> Movimiento:

    #     movimiento = Movimiento(
    #         id=data["id"],
    #         fecha=date.fromisoformat(
    #             data["fecha"]
    #         ),
    #         descripcion=data["descripcion"],
    #     )

    #     movimiento.estado = EstadoMovimiento(
    #         data["estado"]
    #     )

    #     return movimiento

    def _from_dict(
        self,
        data: dict,
    ) -> Movimiento:

        movimiento = Movimiento(
            id=data["id"],
            fecha=date.fromisoformat(
                data["fecha"]
            ),
            descripcion=data["descripcion"],
        )

        # movimiento.estado = EstadoMovimiento(
        #     data["estado"]
        # )

        for item in data["lineas"]:

            cuenta = (
                self.plan_cuenta_repository
                .buscar_por_codigo(
                    item["codigo_cuenta"]
                )
            )

            importe = Decimal(
                item["importe"]
            )

            if (
                item["tipo_afectacion"]
                == TipoAfectacion.DEBITO.value
            ):

                linea = LineaMovimiento.debito(
                    cuenta,
                    importe,
                )

            else:

                linea = LineaMovimiento.credito(
                    cuenta,
                    importe,
                )

            movimiento.agregar_linea(
                linea
            )
        movimiento.estado = EstadoMovimiento(
            data["estado"]
        )
        return movimiento
        