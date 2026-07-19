from datetime import date

from domain.entities.ejercicio_contable import (
    EjercicioContable,
)

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)


class EjercicioContableMapper:

    @staticmethod
    def to_dict(
        ejercicio,
    ):
        return {
            "id": ejercicio.id,
            "empresa_id": ejercicio.empresa_id,
            "fecha_inicio": ejercicio.fecha_inicio.isoformat(),
            "fecha_fin": ejercicio.fecha_fin.isoformat(),
            "estado": ejercicio.estado.name,
        }



    def test_mapper_convierte_dict_a_entidad():

        datos = {
            "id": 1,
            "empresa_id": 7,
            "fecha_inicio": "2026-01-01",
            "fecha_fin": "2026-12-31",
            "estado": "ABIERTO",
        }

        ejercicio = EjercicioContableMapper.from_dict(
            datos,
        )

        assert ejercicio.id == 1

        assert ejercicio.empresa_id == 7

        assert ejercicio.fecha_inicio == date(
            2026,
            1,
            1,
        )

        assert ejercicio.fecha_fin == date(
            2026,
            12,
            31,
        )

        assert (
            ejercicio.estado
            == EstadoEjercicio.ABIERTO
        )
        
    @staticmethod
    def from_dict(
        datos,
    ):
        return EjercicioContable(
            id=datos["id"],
            empresa_id=datos["empresa_id"],
            fecha_inicio=date.fromisoformat(
                datos["fecha_inicio"],
            ),
            fecha_fin=date.fromisoformat(
                datos["fecha_fin"],
            ),
            estado=EstadoEjercicio[
                datos["estado"]
            ],
        )
    
    @staticmethod
    def to_dict_list(
        ejercicios,
    ):
        return [
            EjercicioContableMapper.to_dict(
                ejercicio,
            )
            for ejercicio in ejercicios
        ]
    @staticmethod
    def from_dict_list(
        datos,
    ):
        return [
            EjercicioContableMapper.from_dict(
                dato,
            )
            for dato in datos
        ]