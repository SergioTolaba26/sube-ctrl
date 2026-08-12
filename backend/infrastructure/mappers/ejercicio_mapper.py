from datetime import date

from domain.entities.ejercicio import (
    Ejercicio,
)

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)


class EjercicioMapper:

    @staticmethod
    def to_dict(
        ejercicio: Ejercicio,
    ):

        return {
            "id": ejercicio.id,
            "empresa_id": ejercicio.empresa_id,
            "anio": ejercicio.anio,
            "fecha_apertura": (
                ejercicio.fecha_apertura.isoformat()
                if ejercicio.fecha_apertura
                else None
            ),
            "fecha_cierre": (
                ejercicio.fecha_cierre.isoformat()
                if ejercicio.fecha_cierre
                else None
            ),
            "estado": ejercicio.estado.name,
        }

    @staticmethod
    def from_dict(
        datos: dict,
    ) -> Ejercicio:

        return Ejercicio(
            id=datos["id"],
            empresa_id=datos["empresa_id"],
            anio=datos["anio"],
            fecha_apertura=(
                date.fromisoformat(
                    datos["fecha_apertura"],
                )
                if datos["fecha_apertura"]
                else None
            ),
            fecha_cierre=(
                date.fromisoformat(
                    datos["fecha_cierre"],
                )
                if datos["fecha_cierre"]
                else None
            ),
            estado=EstadoEjercicio[
                datos["estado"]
            ],
        )

    @staticmethod
    def to_dict_list(
        ejercicios: list[Ejercicio],
    ) -> list[dict]:

        return [
            EjercicioMapper.to_dict(
                ejercicio,
            )
            for ejercicio in ejercicios
        ]

    @staticmethod
    def from_dict_list(
        datos: list[dict],
    ) -> list[Ejercicio]:

        return [
            EjercicioMapper.from_dict(
                dato,
            )
            for dato in datos
        ]