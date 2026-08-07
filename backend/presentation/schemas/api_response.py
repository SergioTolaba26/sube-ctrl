from typing import Generic
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(
    BaseModel,
    Generic[T],
):

    mensaje: str

    data: T