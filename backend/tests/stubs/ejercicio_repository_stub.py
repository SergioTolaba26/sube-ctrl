
from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)


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

    def buscar_por_anio(
        self,
        empresa_id: int,
        anio: int,
    ):

        for ejercicio in self.ejercicios:

            if (
                ejercicio.empresa_id == empresa_id
                and ejercicio.anio == anio
            ):
                return ejercicio

        return None

    def buscar_abierto(
        self,
        empresa_id: int,
    ):

        for ejercicio in self.ejercicios:

            if (
                ejercicio.empresa_id == empresa_id
                and ejercicio.estado
                == EstadoEjercicio.ABIERTO
            ):
                return ejercicio

        return None

    def eliminar(
        self,
        id_,
    ):

        self.ejercicios = [
            ejercicio
            for ejercicio in self.ejercicios
            if ejercicio.id != id_
        ]

    def actualizar(
        self,
        ejercicio,
    ):

        for indice, existente in enumerate(
            self.ejercicios
        ):

            if existente.id == ejercicio.id:
                self.ejercicios[indice] = ejercicio
                return

