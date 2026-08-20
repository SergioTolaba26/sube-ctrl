from domain.entities.cuenta import Cuenta
from infrastructure.persistence.base.storage import (
    Storage,
)

from infrastructure.mappers.cuenta_mapper import (
    CuentaMapper,
)

from infrastructure.repositories.json.base_repository import (
    BaseRepositoryJson,
)


class CuentaRepositoryJson(
    BaseRepositoryJson,
):

    def __init__(
        self,
        storage: Storage,
    ):
        super().__init__(
            storage=storage,
            mapper=CuentaMapper,
        )

    # =========================================================
    # LISTAR
    # =========================================================

    def listar(
        self,
        empresa_id: int,
    ):

        cuentas = super().listar()

        return [
            cuenta
            for cuenta in cuentas
            if cuenta.empresa_id == empresa_id
        ]

    # =========================================================
    # BUSCAR POR ID
    # =========================================================

    def buscar_por_id(
        self,
        empresa_id: int,
        cuenta_id: int,
    ):

        cuentas = self.listar(
            empresa_id,
        )

        for cuenta in cuentas:

            if cuenta.id == cuenta_id:
                return cuenta

        return None

    # =========================================================
    # BUSCAR POR CODIGO
    # =========================================================

    def buscar_por_codigo(
        self,
        empresa_id: int,
        codigo: str,
    ):

        cuentas = self.listar(
            empresa_id,
        )

        for cuenta in cuentas:

            if cuenta.codigo == codigo:
                return cuenta

        return None

    # =========================================================
    # MODIFICAR
    # =========================================================

    def modificar(
        self,
        empresa_id: int,
        cuenta: Cuenta,
    ) -> None:

        cuentas = self._listar_todas()

        modificada = False

        for i, existente in enumerate(cuentas):

            if (
                existente.empresa_id == empresa_id
                and existente.id == cuenta.id
            ):

                cuentas[i] = cuenta

                modificada = True

                break

        if not modificada:
            return

        datos = self.mapper.to_dict_list(
            cuentas,
        )

        self.storage.save(
            datos,
        )

    # =========================================================
    # ELIMINAR
    # =========================================================

    def eliminar(
        self,
        empresa_id: int,
        cuenta_id: int,
    ) -> None:

        cuentas = self._listar_todas()

        cuentas_filtradas = [
            cuenta
            for cuenta in cuentas
            if not (
                cuenta.empresa_id == empresa_id
                and cuenta.id == cuenta_id
            )
        ]

        datos = self.mapper.to_dict_list(
            cuentas_filtradas,
        )

        self.storage.save(
            datos,
        )