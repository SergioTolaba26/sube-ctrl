from domain.entities.cuenta import Cuenta

from domain.services.cuenta_service import (
    CuentaService,
)
from domain.enums.tipo_cuenta import (
    TipoCuenta,
)

class RegistrarCuenta:

    def __init__(
        self,
        service: CuentaService,
    ):
        self.service = service

    def execute(
        self,
        codigo: str,
        nombre: str,
        tipo,
        imputable: bool = True,
        empresa_id: int = 1,
    ):

        
        if isinstance(
        tipo,
        str,
    ):
            
            tipo = TipoCuenta[tipo]

        cuenta = Cuenta(
            id=None,
            #empresa_id= 1,
            empresa_id=empresa_id,
            codigo=codigo,
            nombre=nombre,
            tipo=tipo,
            imputable=imputable,
        )

        self.service.guardar(
            cuenta,
        )

        return cuenta