from enum import Enum


class TipoAfectacion(str, Enum):
    """
    Indica cómo una línea afecta una cuenta.
    """

    DEBITO = "DEBITO"
    CREDITO = "CREDITO"