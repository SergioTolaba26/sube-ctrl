from domain.entities.movimiento import (
    Movimiento,
)


class MovimientoService:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    def listar(
        self,
    ) -> list[Movimiento]:

        return self.repository.listar()

    def listar_por_fecha(
        self,
        desde,
        hasta,
    ) -> list[Movimiento]:

        return self.repository.listar_por_fecha(
            desde,
            hasta,
        )

    def buscar_por_id(
        self,
        id_,
    ):

        return self.repository.buscar_por_id(
            id_,
        )

    def guardar(
        self,
        movimiento,
    ):

        if movimiento.id is None:

            movimientos = self.repository.listar()

            if not movimientos:

                movimiento.id = 1

            else:

                movimiento.id = (
                    max(
                        m.id
                        for m in movimientos
                    )
                    + 1
                )

        #
        # Generar número de asiento
        #
        if movimiento.numero_asiento == 0:

            movimientos = self.repository.listar()

            if not movimientos:

                movimiento.numero_asiento = 1

            else:

                movimiento.numero_asiento = (
                    max(
                        m.numero_asiento
                        for m in movimientos
                    )
                    + 1
                )

        #
        # ← ESTE GUARDAR VA AFUERA
        #
        self.repository.guardar(
            movimiento,
        )
    def eliminar(
        self,
        id_,
    ):

        self.repository.eliminar(
            id_,
        )