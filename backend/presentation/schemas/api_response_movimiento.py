from pydantic import BaseModel

from presentation.schemas.movimiento_schema import (
    MovimientoResponse,
)


class ApiResponseMovimiento(
    BaseModel,
):

    mensaje: str

    data: MovimientoResponse