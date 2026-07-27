import sys
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from application.factory import (
    ApplicationFactory,
)

from domain.entities.ejercicio import (
    Ejercicio,
)

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)

factory = ApplicationFactory()

service = factory.ejercicio_service


def crear_si_no_existe(
    anio: int,
):

    existente = service.repository.buscar_por_anio(
        anio,
    )

    if existente:

        print(
            f"[YA EXISTE] Ejercicio {anio}",
        )

        return

    ejercicio = Ejercicio(
        anio=anio,
        fecha_apertura=date(
            anio,
            1,
            1,
        ),
        fecha_cierre=None,
        estado=EstadoEjercicio.ABIERTO,
    )

    service.guardar(
        ejercicio,
    )

    print(
        f"[CREADO] Ejercicio {anio}",
    )


if __name__ == "__main__":

    crear_si_no_existe(
        2026,
    )