from persistence.repositories.ejercicio_repository_json import (
    EjercicioRepositoryJson,
)


def test_crea_repositorio():

    repo = EjercicioRepositoryJson()

    assert repo is not None


from datetime import date

from domain.entities.ejercicio_contable import (
    EjercicioContable,
)

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)

from persistence.repositories.ejercicio_repository_json import (
    EjercicioRepositoryJson,
)


def test_convierte_ejercicio_a_dict():

    repo = EjercicioRepositoryJson()

    ejercicio = EjercicioContable(
        id=1,
        empresa_id=7,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
        estado=EstadoEjercicio.ABIERTO,
    )

    data = repo._to_dict(
        ejercicio
    )

    assert data == {

        "id": 1,

        "empresa_id": 7,

        "fecha_inicio": "2026-01-01",

        "fecha_fin": "2026-12-31",

        "estado": "ABIERTO",
    }

from datetime import date

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)


def test_convierte_dict_a_ejercicio():

    repo = EjercicioRepositoryJson()

    data = {

        "id": 1,

        "empresa_id": 7,

        "fecha_inicio": "2026-01-01",

        "fecha_fin": "2026-12-31",

        "estado": "ABIERTO",
    }

    ejercicio = repo._from_dict(data)

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

from datetime import date
import json

from domain.entities.ejercicio_contable import (
    EjercicioContable,
)

from persistence.repositories.ejercicio_repository_json import (
    EjercicioRepositoryJson,
)


def test_guardar_ejercicio(tmp_path):

    archivo = tmp_path / "ejercicios.json"

    archivo.write_text(
        '{"ejercicios": []}',
        encoding="utf-8",
    )

    repo = EjercicioRepositoryJson(archivo)

    ejercicio = EjercicioContable(
        id=1,
        empresa_id=7,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
    )

    repo.guardar(
        ejercicio
    )

    data = json.loads(
        archivo.read_text(
            encoding="utf-8"
        )
    )

    assert len(
        data["ejercicios"]
    ) == 1

    assert (
        data["ejercicios"][0]["empresa_id"]
        == 7
    )

def test_obtener_todos(tmp_path):

    archivo = tmp_path / "ejercicios.json"

    archivo.write_text(
        """
{
    "ejercicios": [
        {
            "id": 1,
            "empresa_id": 7,
            "fecha_inicio": "2026-01-01",
            "fecha_fin": "2026-12-31",
            "estado": "ABIERTO"
        }
    ]
}
""",
        encoding="utf-8",
    )
    repo = EjercicioRepositoryJson(archivo)
    #repo = EmpresaRepositoryJson(archivo)

    ejercicios = repo.obtener_todos()

    assert len(ejercicios) == 1

    assert ejercicios[0].empresa_id == 7

    assert ejercicios[0].id == 1

from datetime import date


def test_obtener_ejercicio_abierto(tmp_path):

    archivo = tmp_path / "ejercicios.json"

    archivo.write_text(
        """
{
    "ejercicios": [
        {
            "id": 1,
            "empresa_id": 7,
            "fecha_inicio": "2025-01-01",
            "fecha_fin": "2025-12-31",
            "estado": "CERRADO"
        },
        {
            "id": 2,
            "empresa_id": 7,
            "fecha_inicio": "2026-01-01",
            "fecha_fin": "2026-12-31",
            "estado": "ABIERTO"
        }
    ]
}
""",
        encoding="utf-8",
    )

    repo = EjercicioRepositoryJson(archivo)

    ejercicio = repo.obtener_abierto()

    assert ejercicio is not None

    assert ejercicio.id == 2

    assert ejercicio.esta_abierto()

def test_eliminar_ejercicio(tmp_path):

    archivo = tmp_path / "ejercicios.json"

    archivo.write_text(
        """
{
    "ejercicios": [
        {
            "id": 1,
            "empresa_id": 7,
            "fecha_inicio": "2026-01-01",
            "fecha_fin": "2026-12-31",
            "estado": "ABIERTO"
        }
    ]
}
""",
        encoding="utf-8",
    )

    repo = EjercicioRepositoryJson(archivo)

    ejercicio = repo.obtener_todos()[0]

    repo.eliminar(ejercicio)

    ejercicios = repo.obtener_todos()

    assert len(ejercicios) == 0

# Inicio refactorizacion para simplificar codigo Sprint 10.8 Refactor
