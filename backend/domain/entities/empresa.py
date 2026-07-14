from pydantic import Field

from domain.base.entity import Entity


class Empresa(Entity):

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

    activa: bool = Field(
        default=True,
    )


    def activar(self) -> None:
        """
        Activa la empresa.
        """
        self.activa = True


    def desactivar(self) -> None:
        """
        Desactiva la empresa.
        """
        self.activa = False

    