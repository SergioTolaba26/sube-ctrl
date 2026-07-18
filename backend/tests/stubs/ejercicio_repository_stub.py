class EjercicioRepositoryStub:

    def __init__(self):

        self.ejercicios = []

    def guardar(
        self,
        ejercicio,
    ):

        self.ejercicios.append(
            ejercicio
        )
    def buscar_por_id(
        self,
        ejercicio_id: int,
    ):

        for ejercicio in self.ejercicios:

            if ejercicio.id == ejercicio_id:
                return ejercicio

        return None
    def obtener_todas(
        self,
    ):

        return self.ejercicios