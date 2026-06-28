from pydantic import BaseModel, Field


class Tarifa(BaseModel):
    id: int = Field(..., gt=0)
    nombre: str = Field(..., min_length=1, max_length=50)
    valor: float = Field(..., ge=0)


class TarifaUpdate(BaseModel):
    valor: float = Field(..., ge=0)