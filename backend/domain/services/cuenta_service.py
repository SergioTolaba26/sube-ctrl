from domain.entities.cuenta import (
    Cuenta,
)


class CuentaService:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    def listar(
        self,
    ) -> list[Cuenta]:

        return self.repository.listar()

    def buscar_por_id(
        self,
        id_,
    ):

        return self.repository.buscar_por_id(
            id_,
        )

    def buscar_por_codigo(
        self,
        codigo,
    ):

        return self.repository.buscar_por_codigo(
            codigo,
        )

    # def guardar(
    #     self,
    #     cuenta,
    # ):

    #     self.repository.guardar(
    #         cuenta,
    #     )

    def guardar(
        self,
        cuenta,
    ):

        if cuenta.id is None:

            cuentas = self.repository.listar()

            if not cuentas:

                cuenta.id = 1

            else:

                cuenta.id = (
                    max(
                        c.id
                        for c in cuentas
                    )
                    + 1
                )

        self.repository.guardar(
            cuenta,
        )

    def eliminar(
        self,
        id_,
    ):

        self.repository.eliminar(
            id_,
        )