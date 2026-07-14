from domain.services.balance_sumas_saldos import (
    BalanceSumasSaldos,
)

from domain.services.libro_mayor import (
    LibroMayor,
)

from domain.value_objects.cuenta_mayor import (
    CuentaMayor,
)


class ConsultarLibroMayor:

    def ejecutar(
        self,
        movimientos,
    ):

        filas = (
            BalanceSumasSaldos()
            .obtener(
                movimientos=movimientos,
            )
        )

        mayor = LibroMayor()

        cuentas = []

        for fila in filas:

            renglones = mayor.obtener(
                cuenta=fila.cuenta,
                movimientos=movimientos,
            )

            saldo = (
                renglones[-1].saldo
                if renglones
                else 0
            )

            cuentas.append(
                CuentaMayor(
                    cuenta=fila.cuenta,
                    renglones=renglones,
                    saldo=saldo,
                )
            )

        return cuentas