from datetime import date

from fastapi import APIRouter

from application.factory import (
ApplicationFactory,
)

from presentation.schemas.movimiento_schema import (
MovimientoResponse,
)

from presentation.mappers.movimiento_response_mapper import (
MovimientoResponseMapper,
)

router = APIRouter(
prefix="/libro-diario",
tags=["Libro Diario"],
)

factory = ApplicationFactory()

@router.get(
"/",
response_model=list[MovimientoResponse],
)
def listar_libro_diario(
    desde: date | None = None,
    hasta: date | None = None,
    ):


    use_case = factory.listar_libro_diario()

    movimientos = use_case.execute(
        desde=desde,
        hasta=hasta,
    )

    return [
        MovimientoResponseMapper.to_resumen(
            movimiento,
        )
        for movimiento in movimientos
    ]

