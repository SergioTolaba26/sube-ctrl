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
        empresa_id: int,
    ) -> list[Cuenta]:

        return self.repository.listar(
            empresa_id,
        )

    def buscar_por_id(
        self,
        empresa_id: int,
        cuenta_id: int | None = None,
    ):

        if cuenta_id is None:

            cuenta_id = empresa_id

            return self.repository.buscar_por_id(
                cuenta_id,
            )

        return self.repository.buscar_por_id(
            empresa_id,
            cuenta_id,
        )
    # *****************************************************
    def buscar_por_codigo(
        self,
        empresa_id: int,
        codigo: str,
    ) -> Cuenta | None:

        return self.repository.buscar_por_codigo(
            empresa_id,
            codigo,
        )

    def guardar(
        self,
        cuenta: Cuenta,
    ) -> None:

        if cuenta.id is None:

            cuentas = self.repository.listar(
                cuenta.empresa_id,
            )

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

    def modificar(
        self,
        empresa_id: int,
        cuenta: Cuenta,
    ) -> Cuenta | None:

        return self.repository.modificar(
            empresa_id,
            cuenta,
        )

    def eliminar(
        self,
        empresa_id: int,
        cuenta_id: int,
    ) -> Cuenta | None:

        return self.repository.eliminar(
            empresa_id,
            cuenta_id,
        )