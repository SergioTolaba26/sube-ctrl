from pathlib import Path

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta
from domain.repositories.plan_cuenta_repository import (
    PlanCuentaRepository,
)

from persistence.repositories.base_repository_json import (
    BaseRepositoryJson,
)


class PlanCuentaRepositoryJson(
    BaseRepositoryJson,
    PlanCuentaRepository,
):

    def __init__(
        self,
        file_path: Path | None = None,
    ):

        if file_path is None:

            file_path = Path(
                "data/plan_cuentas.json"
            )

        super().__init__(
            file_path,
            "cuentas",
        )

    def obtener_todas(
        self,
    ) -> list[Cuenta]:

        return self.obtener_todos()

    # def buscar_por_codigo(
    #     self,
    #     codigo: str,
    # ) -> Cuenta | None:

    #     raise NotImplementedError
    def buscar_por_codigo(
        self,
        codigo: str,
    ) -> Cuenta | None:

        for cuenta in self.obtener_todas():

            if cuenta.codigo == codigo:

                return cuenta

        return None
   

    def _to_dict(
        self,
        cuenta: Cuenta,
    ) -> dict:

        return {

            "id": cuenta.id,

            "empresa_id": cuenta.empresa_id,

            "codigo": cuenta.codigo,

            "nombre": cuenta.nombre,

            "tipo": cuenta.tipo.name,

            "activa": cuenta.activa,

        }
    def _from_dict(
        self,
        data: dict,
    ) -> Cuenta:

        return Cuenta(

            id=data["id"],
            empresa_id=data["empresa_id"],
            codigo=data["codigo"],

            nombre=data["nombre"],

            tipo=TipoCuenta[
                data["tipo"]
            ],

            activa=data["activa"],

        )
    