from enum import Enum


class TipoCuenta(Enum):
    ACTIVO = "ACTIVO"
    PASIVO = "PASIVO"
    PATRIMONIO = "PATRIMONIO"
    INGRESO = "INGRESO"
    GASTO = "GASTO"

    def es_naturaleza_deudora(self) -> bool:
        """
        Indica si la cuenta posee naturaleza deudora.
        """
        return self in (
            TipoCuenta.ACTIVO,
            TipoCuenta.GASTO,
        )