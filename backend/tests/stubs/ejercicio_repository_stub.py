from domain.enums.estado_ejercicio import EstadoEjercicio


class EjercicioRepositoryStub:

    def __init__(self):

        self.ejercicios = []

    def guardar(
        self,
        ejercicio,
    ):

        self.ejercicios.append(
            ejercicio,
        )

    def buscar_por_id(
        self,
        ejercicio_id: int,
    ):

        for ejercicio in self.ejercicios:

            if ejercicio.id == ejercicio_id:
                return ejercicio

        return None

    def listar(
        self,
    ):

        return self.ejercicios

    # Compatibilidad temporal
    def obtener_todas(
        self,
    ):

        return self.listar()
    
    def buscar_por_anio(
        self,
        anio: int,
    ):

        for ejercicio in self.ejercicios:

            if ejercicio.anio == anio:
                return ejercicio

        return None


    def buscar_abierto(
        self,
    ):

        for ejercicio in self.ejercicios:

            if (
                ejercicio.estado
                == EstadoEjercicio.ABIERTO
            ):
                return ejercicio

        return None