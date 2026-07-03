from pydantic import BaseModel


class Entity(BaseModel):
    """
    Entidad base del dominio.
    Todas las entidades persistentes deben heredar de esta clase.
    """

    id: int