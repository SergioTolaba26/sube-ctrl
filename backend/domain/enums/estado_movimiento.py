from enum import Enum


class EstadoMovimiento(str, Enum):
    BORRADOR = "BORRADOR"
    CONFIRMADO = "CONFIRMADO"
    ANULADO = "ANULADO"