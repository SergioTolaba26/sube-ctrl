from datetime import date

from domain.entities.movimiento import Movimiento


class CerrarEjercicio:

    def ejecutar(
        self,
        ejercicio,
        movimientos,
    ):

        movimiento = Movimiento(  # return Movimiento(
            id=None,
            fecha=date.today(),
            descripcion="Cierre del ejercicio",
        )
        movimiento.confirmar() # falla porque no se puede confirmar un movimiento sin lineas

        return movimiento
    # Entonces la secuencia es Crear movimiento es lo que ya hicimos, generar lineas, balancear, confirmar
    # Todo esto quiere decir que hay que confeccionar el asiento de cierre antes de confirmarlo