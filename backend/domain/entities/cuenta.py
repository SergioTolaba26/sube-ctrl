from pydantic import Field

from domain.base.entity import Entity

from domain.enums.tipo_cuenta import TipoCuenta


class Cuenta(Entity):
    """
    Representa un recurso económico del negocio.

    Una Cuenta no almacena su saldo.
    El saldo se obtiene a partir de las Líneas de Movimiento.
    """

    codigo: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Código único de la cuenta."
    )

    nombre: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Nombre descriptivo de la cuenta."
    )

    tipo: TipoCuenta = Field(
        ...,
        description="Tipo de cuenta."
    )

    activa: bool = Field(
        default=True,
        description="Indica si la cuenta puede utilizarse."
    )
    imputable: bool = Field(
    default=True,
    description="Indica si la cuenta admite movimientos."
)
    def activar(self) -> None:
        """Activa la cuenta."""
        self.activa = True

    def desactivar(self) -> None:
        """Desactiva la cuenta."""
        self.activa = False

    def hacer_no_imputable(self) -> None:
        """
        Impide que la cuenta reciba movimientos.
        """
        self.imputable = False

    def hacer_imputable(self) -> None:
        """
        Permite nuevamente registrar movimientos en la cuenta.
        """
        self.imputable = True

    def es_imputable(self) -> bool:
        """
        Indica si la cuenta admite recibir movimientos.
        """
        return self.imputable

    def esta_activa(self) -> bool:
        """Indica si la cuenta está activa."""
        return self.activa

    def renombrar(self, nuevo_nombre: str) -> None:
        """
        Cambia el nombre de la cuenta.
        """

        nuevo_nombre = nuevo_nombre.strip()

        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacío.")

        self.nombre = nuevo_nombre

    