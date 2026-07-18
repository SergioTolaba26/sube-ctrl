from infrastructure.persistence.base.storage import (
    Storage,
)


def test_crea_storage():

    storage = Storage(
        "data/test.json",
    )

    assert storage.file_path.name == "test.json"

import json

from infrastructure.persistence.base.storage import (
    Storage,
)


def test_read_devuelve_lista(tmp_path):

    archivo = tmp_path / "datos.json"

    archivo.write_text(
        json.dumps(
            [
                {"id": 1},
                {"id": 2},
            ]
        ),
        encoding="utf-8",
    )

    storage = Storage(
        archivo,
    )

    #datos = storage.read()
    datos = storage.load()
    assert datos == [
        {"id": 1},
        {"id": 2},
    ]


import json

from infrastructure.persistence.base.storage import (
    Storage,
)


def test_save_guarda_lista(tmp_path):

    archivo = tmp_path / "datos.json"

    storage = Storage(
        archivo,
    )

    datos = [
        {"id": 1},
        {"id": 2},
    ]

    storage.save(
        datos,
    )

    contenido = json.loads(
        archivo.read_text(
            encoding="utf-8",
        )
    )

    assert contenido == datos

def test_load_devuelve_lista_vacia_si_no_existe(tmp_path):

    archivo = tmp_path / "inexistente.json"

    storage = Storage(
        archivo,
    )

    datos = storage.load()

    assert datos == []

def test_save_crea_directorios(tmp_path):

    archivo = (
        tmp_path
        / "empresa"
        / "cuentas"
        / "datos.json"
    )

    storage = Storage(
        archivo,
    )

    storage.save(
        [
            {"id": 1},
        ]
    )

    assert archivo.exists()

def test_load_devuelve_lista_vacia_si_el_archivo_esta_vacio(
    tmp_path,
):

    archivo = tmp_path / "datos.json"

    archivo.write_text(
        "",
        encoding="utf-8",
    )

    storage = Storage(
        archivo,
    )

    datos = storage.load()

    assert datos == []

import json


def test_save_escribe_correctamente_con_reemplazo_atomico(
    tmp_path,
):

    archivo = tmp_path / "datos.json"

    storage = Storage(
        archivo,
    )

    storage.save(
        [
            {"id": 1},
            {"id": 2},
        ]
    )

    contenido = json.loads(
        archivo.read_text(
            encoding="utf-8",
        )
    )

    assert contenido == [
        {"id": 1},
        {"id": 2},
    ]

    assert not (
        tmp_path / "datos.json.tmp"
    ).exists()

    