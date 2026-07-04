from pydantic import BaseModel, ConfigDict


class Entity(BaseModel):
    """
    Entidad base del dominio.
    Todas las entidades persistentes deben heredar de esta clase.
    """

    model_config = ConfigDict(validate_assignment=True)

    id: int | None = None