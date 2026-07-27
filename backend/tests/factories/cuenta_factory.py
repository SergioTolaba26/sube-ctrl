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

    @staticmethod
    def caja():

        return CuentaFactory.crear(
            id=1,
            codigo="1.1.01",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )

    @staticmethod
    def banco():

        return CuentaFactory.crear(
            id=2,
            codigo="1.1.02",
            nombre="Banco",
            tipo=TipoCuenta.ACTIVO,
        )

    @staticmethod
    def clientes():

        return CuentaFactory.crear(
            id=3,
            codigo="1.2.01",
            nombre="Clientes",
            tipo=TipoCuenta.ACTIVO,
        )

    @staticmethod
    def mercaderias():

        return CuentaFactory.crear(
            id=4,
            codigo="1.3.01",
            nombre="Mercaderías",
            tipo=TipoCuenta.ACTIVO,
        )

    @staticmethod
    def proveedores():

        return CuentaFactory.crear(
            id=5,
            codigo="2.1.01",
            nombre="Proveedores",
            tipo=TipoCuenta.PASIVO,
        )

    @staticmethod
    def capital():

        return CuentaFactory.crear(
            id=7,
            codigo="3.1.01",
            nombre="Capital",
            tipo=TipoCuenta.PATRIMONIO,
        )

    @staticmethod
    def resultados_acumulados():

        return CuentaFactory.crear(
            id=8,
            codigo="3.2.01",
            nombre="Resultados Acumulados",
            tipo=TipoCuenta.PATRIMONIO,
        )

    @staticmethod
    def ventas():

        return CuentaFactory.crear(
            id=9,
            codigo="4.1.01",
            nombre="Ventas",
            tipo=TipoCuenta.INGRESO,
        )

    @staticmethod
    def compras():

        return CuentaFactory.crear(
            id=11,
            codigo="5.1.01",
            nombre="Compras",
            tipo=TipoCuenta.GASTO,
        )

    @staticmethod
    def alquiler():

        return CuentaFactory.crear(
            id=13,
            codigo="5.3.01",
            nombre="Alquiler",
            tipo=TipoCuenta.GASTO,
        )