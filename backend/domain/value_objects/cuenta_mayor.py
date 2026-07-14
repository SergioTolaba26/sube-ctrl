from dataclasses import dataclass

from decimal import Decimal

from domain.entities.cuenta import Cuenta

from domain.value_objects.renglon_libro_mayor import (
    RenglonLibroMayor,
)


@dataclass(slots=True)
class CuentaMayor:

    cuenta: Cuenta

    renglones: list[RenglonLibroMayor]

    saldo: Decimal