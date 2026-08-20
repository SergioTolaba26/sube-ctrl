class BaseRepositoryJson:

    def __init__(
        self,
        storage,
        mapper,
    ):
        self.storage = storage
        self.mapper = mapper
    def _listar_todas(self):

        datos = self.storage.load()

        return self.mapper.from_dict_list(
            datos,
        )
    def listar(
        self,
    ):

        datos = self.storage.load()

        return self.mapper.from_dict_list(
            datos,
        )
    def buscar_por_id(
        self,
        id_,
    ):

        for entidad in self._listar_todas():

            if entidad.id == id_:
                return entidad

        return None


    def guardar(
        self,
        entidad,
    ):

        entidades = self._listar_todas()

        reemplazada = False

        for i, existente in enumerate(entidades):

            if existente.id == entidad.id:

                entidades[i] = entidad

                reemplazada = True

                break

        if not reemplazada:

            entidades.append(entidad)

        datos = self.mapper.to_dict_list(
            entidades,
        )

        self.storage.save(
            datos,
        )   
    def modificar(
        self,
        entidad,
    ):

        self.guardar(
            entidad,
        )

    def eliminar(
        self,
        id_,
    ):

        entidades = [
            entidad
            for entidad in self._listar_todas()
            if entidad.id != id_
        ]

        datos = self.mapper.to_dict_list(
            entidades,
        )

        self.storage.save(
            datos,
        )