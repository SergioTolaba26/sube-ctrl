from domain.repositories.plan_cuenta_repository import (
    PlanCuentaRepository,
)

from tests.builders.entidades_builder import (
    crear_caja,
    crear_ventas,
)


class PlanCuentaRepositoryStub(
    PlanCuentaRepository,
):

    def guardar(self, cuenta):
        pass

    def obtener_todas(self):
        return []

    def eliminar(self, cuenta):
        pass

    def buscar_por_codigo(
        self,
        codigo: str,
    ):

        if codigo == "1.1.01":
            return crear_caja()

        if codigo == "4.1.01":
            return crear_ventas()

        return None