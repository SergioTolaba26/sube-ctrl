from infrastructure.persistence.base.storage import (
    Storage,
)

from infrastructure.mappers.cuenta_mapper import (
    CuentaMapper,
)

#class CuentaRepositoryJson:
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
        storage,
        CuentaMapper,
    )
    # Ya funciona la herencia y puedo borrar este metodo que ahora viene de base_repository.py
    # def listar(
    #     self,
    # ):

    #     datos = self.storage.load()

    #     return CuentaMapper.from_dict_list(
    #         datos,
    #     )
    def buscar_por_codigo(
        self,
        codigo: str,
    ):

        for cuenta in self.listar():

            if cuenta.codigo == codigo:
                return cuenta

        return None
    
    # def guardar(
    #     self,
    #     cuenta,
    # ):

    #     cuentas = self.listar()

    #     # cuentas.append(
    #     #     cuenta,
    #     # )
    #     reemplazada = False

    #     for i, existente in enumerate(cuentas):

    #         if existente.codigo == cuenta.codigo:

    #             cuentas[i] = cuenta

    #             reemplazada = True

    #             break

    #     if not reemplazada:

    #             cuentas.append(
    #             cuenta,
    #         )
    #     datos = CuentaMapper.to_dict_list(
    #         cuentas,
    #     )

    #     self.storage.save(
    #         datos,
    #     )

    # def buscar_por_id(
    #     self,
    #     id_,
    # ):

    #     for cuenta in self.listar():

    #         if cuenta.id == id_:
    #             return cuenta

    #     return None
    
    # def eliminar(
    #     self,
    #     id_,
    # ):

    #     cuentas = [
    #         cuenta
    #         for cuenta in self.listar()
    #         if cuenta.id != id_
    #     ]

    #     datos = CuentaMapper.to_dict_list(
    #         cuentas,
    #     )

    #     self.storage.save(
    #         datos,
    #     )