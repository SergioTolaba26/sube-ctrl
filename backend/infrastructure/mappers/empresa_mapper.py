from domain.entities.empresa import Empresa
class EmpresaMapper:

    @staticmethod
    def to_dict(
        empresa,
    ):
        return {
            "id": empresa.id,
            "razon_social": empresa.razon_social,
            "nombre_fantasia": empresa.nombre_fantasia,
            "cuit": empresa.cuit,
            "activa": empresa.activa,
        }
    
    @staticmethod
    def from_dict(
        datos,
    ):
        return Empresa(
            id=datos["id"],
            razon_social=datos["razon_social"],
            nombre_fantasia=datos["nombre_fantasia"],
            cuit=datos["cuit"],
            activa=datos["activa"],
        )
    
    @staticmethod
    def to_dict_list(
        empresas,
    ):
        return [
            EmpresaMapper.to_dict(
                empresa,
            )
            for empresa in empresas
        ]
    
    @staticmethod
    def from_dict_list(
        datos,
    ):
        return [
            EmpresaMapper.from_dict(
                item,
            )
            for item in datos
        ]