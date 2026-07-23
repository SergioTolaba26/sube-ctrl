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
    def listar(self):
        return self.cuentas
    
    def buscar_por_id(
        self,
        id_,
    ):

        for cuenta in self.cuentas:

            if cuenta.id == id_:
                return cuenta

        return None