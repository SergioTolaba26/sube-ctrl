from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta

class CuentaMapper:

    @staticmethod
    def to_dict(
        cuenta: Cuenta,
    ):

        return {
            "id": cuenta.id,
            "codigo": cuenta.codigo,
            "nombre": cuenta.nombre,
            "tipo": cuenta.tipo.name,
            "activa": cuenta.activa,
        }
    
    @staticmethod
    def from_dict(
        datos: dict,
    ) -> Cuenta:

        return Cuenta(
            id=datos["id"],
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            tipo=TipoCuenta[
                datos["tipo"]
            ],
            activa=datos["activa"],
        )
    
    @staticmethod
    def to_dict_list(
        cuentas: list[Cuenta],
    ) -> list[dict]:

        return [
            CuentaMapper.to_dict(
                cuenta,
            )
            for cuenta in cuentas
        ]
    @staticmethod
    def from_dict_list(
        datos: list[dict],
    ) -> list[Cuenta]:

        return [
            CuentaMapper.from_dict(
                dato,
            )
            for dato in datos
        ]
    