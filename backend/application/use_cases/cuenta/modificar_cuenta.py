from domain.services.cuenta_service import (
    CuentaService,
)


class ModificarCuenta:

    def __init__(
        self,
        service: CuentaService,
    ):
        self.service = service

    def execute(
        self,
        cuenta_id: int,
        codigo: str,
        nombre: str,
        tipo,
        activa: bool,
        imputable: bool,
        empresa_id: int | None = None,
    ):

        if empresa_id is None:

            cuenta = self.service.buscar_por_id(
                cuenta_id,
            )

        else:

            cuenta = self.service.buscar_por_id(
                empresa_id,
                cuenta_id,
            )

        if cuenta is None:
            return None

        cuenta.codigo = codigo
        cuenta.nombre = nombre
        cuenta.tipo = tipo
        cuenta.activa = activa
        cuenta.imputable = imputable

        self.service.guardar(
            cuenta,
        )

        return cuenta