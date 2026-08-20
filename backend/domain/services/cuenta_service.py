from domain.entities.cuenta import (
    Cuenta,
)


class CuentaService:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    # =========================================================
    # LISTAR
    # =========================================================

    def listar(
        self,
        empresa_id: int,
    ) -> list[Cuenta]:

        return self.repository.listar(
            empresa_id,
        )

    # =========================================================
    # BUSCAR POR ID
    #
    # Compatibilidad:
    #
    # buscar_por_id(cuenta_id)
    #
    # y la nueva forma:
    #
    # buscar_por_id(empresa_id, cuenta_id)
    #
    # La segunda forma se utiliza cuando trabajamos dentro
    # del contexto de una empresa.
    # =========================================================

    def buscar_por_id(
        self,
        empresa_id: int,
        cuenta_id: int | None = None,
    ) -> Cuenta | None:

        if cuenta_id is None:

            return self.repository.buscar_por_id(
                empresa_id,
            )

        return self.repository.buscar_por_id(
            empresa_id,
            cuenta_id,
        )

    # =========================================================
    # BUSCAR POR CODIGO
    # =========================================================

    def buscar_por_codigo(
        self,
        empresa_id: int,
        codigo: str,
    ) -> Cuenta | None:

        return self.repository.buscar_por_codigo(
            empresa_id,
            codigo,
        )

    # =========================================================
    # GUARDAR
    #
    # El ID es responsabilidad de PostgreSQL.
    # Si cuenta.id es None, el repositorio PostgreSQL
    # obtiene el ID generado y lo asigna a la cuenta.
    # =========================================================

    def guardar(
        self,
        cuenta: Cuenta,
    ) -> None:

        self.repository.guardar(
            cuenta,
        )

    # =========================================================
    # ELIMINAR
    #
    # Compatibilidad:
    #
    # eliminar(cuenta_id)
    #
    # y la nueva forma:
    #
    # eliminar(empresa_id, cuenta_id)
    # =========================================================

    def eliminar(
        self,
        empresa_id: int,
        cuenta_id: int | None = None,
    ) -> Cuenta | None:

        if cuenta_id is None:

            return self.repository.eliminar(
                empresa_id,
            )

        return self.repository.eliminar(
            empresa_id,
            cuenta_id,
        )