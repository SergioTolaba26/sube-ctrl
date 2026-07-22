from pydantic import BaseModel, Field


class EmpresaCreate(BaseModel):

    razon_social: str = Field(
        ...,
        min_length=1,
        max_length=150,
    )

    nombre_fantasia: str = Field(
        ...,
        min_length=1,
        max_length=150,
    )

    cuit: str = Field(
        ...,
        min_length=11,
        max_length=13,
    )


class EmpresaUpdate(BaseModel):

    razon_social: str | None = Field(
        default=None,
        min_length=1,
        max_length=150,
    )

    nombre_fantasia: str | None = Field(
        default=None,
        min_length=1,
        max_length=150,
    )

    cuit: str | None = Field(
        default=None,
        min_length=11,
        max_length=13,
    )

    activa: bool | None = None


class EmpresaResponse(BaseModel):

    id: int

    razon_social: str

    nombre_fantasia: str

    cuit: str

    activa: bool

    model_config = {
        "from_attributes": True,
    }