
from persistence.repositories.base_repository_json import (
    BaseRepositoryJson,
)
from dataclasses import dataclass


@dataclass
class Dummy:

    id: int

    nombre: str




class DummyRepository(BaseRepositoryJson):

    def _to_dict(self, dummy):

        return {

            "id": dummy.id,

            "nombre": dummy.nombre,

        }

    def _from_dict(self, data):

        return Dummy(

            id=data["id"],

            nombre=data["nombre"],

        )
def test_guarda_objeto(tmp_path):

    archivo = tmp_path / "dummy.json"

    archivo.write_text(
        '{"items": []}',
        encoding="utf-8",
    )

    repo = DummyRepository(
        archivo,
        "items",
    )

    repo.guardar(

        Dummy(
            1,
            "Uno",
        )

    )

    objetos = repo.obtener_todos()

    assert len(objetos) == 1

    assert objetos[0].nombre == "Uno"

def test_elimina_objeto(tmp_path):

    archivo = tmp_path / "dummy.json"

    archivo.write_text(
        '{"items": []}',
        encoding="utf-8",
    )

    repo = DummyRepository(
        archivo,
        "items",
    )

    dummy = Dummy(
        1,
        "Uno",
    )

    repo.guardar(dummy)

    repo.eliminar(dummy)

    objetos = repo.obtener_todos()

    assert len(objetos) == 0