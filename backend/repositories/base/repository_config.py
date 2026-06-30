from dataclasses import dataclass
from typing import Generic, TypeVar

from pydantic import BaseModel

from persistence.base.storage import Storage

T = TypeVar("T", bound=BaseModel)


@dataclass(frozen=True)
class RepositoryConfig(Generic[T]):
    """
    Configuración de un repositorio.
    """

    storage: Storage
    key: str
    model: type[T]