from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta


class CuentaFactory:

    @staticmethod
    def crear(
        id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
        activa=True,
    ):

        return Cuenta(
            id=id,
            codigo=codigo,
            nombre=nombre,
            tipo=tipo,
            activa=activa,
        )