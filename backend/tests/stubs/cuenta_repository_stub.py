from domain.repositories.plan_cuenta_repository import (
    PlanCuentaRepository,
)


class CuentaRepositoryStub(PlanCuentaRepository):

    def __init__(self):
        self.cuentas = []

    def guardar(self, cuenta):
        self.cuentas.append(cuenta)

    def obtener_todas(self):
        return self.cuentas

    def buscar_por_codigo(self, codigo):
        for cuenta in self.cuentas:
            if cuenta.codigo == codigo:
                return cuenta
        return None

    def eliminar(self, cuenta):
        self.cuentas.remove(cuenta)
    # Agregado para que no de error el test con la nueva arquitectura    
    def listar(
        self,
        empresa_id,
    ):
        return [
            cuenta
            for cuenta in self.cuentas
            if cuenta.empresa_id == empresa_id
        ]
    
    def buscar_por_id(
        self,
        empresa_id,
        cuenta_id=None,
    ):

        if cuenta_id is None:

            cuenta_id = empresa_id

            for cuenta in self.cuentas:

                if cuenta.id == cuenta_id:
                    return cuenta

            return None

        for cuenta in self.cuentas:

            if (
                cuenta.id == cuenta_id
                and cuenta.empresa_id == empresa_id
            ):
                return cuenta

        return None