from infrastructure.persistence.base.storage import (
    Storage,
)

from infrastructure.repositories.json.movimiento_repository import (
    MovimientoRepositoryJson,
)


class FakeCuentaRepository:
    pass


def test_crea_repositorio(
    tmp_path,
):

    storage = Storage(
        tmp_path / "movimientos.json",
    )

    repository = MovimientoRepositoryJson(
        storage,
        FakeCuentaRepository(),
    )

    assert repository.storage is storage

    assert repository.cuenta_repository is not None
from datetime import date
from decimal import Decimal

from domain.entities.cuenta import Cuenta
from domain.entities.movimiento import Movimiento

from domain.enums.tipo_cuenta import TipoCuenta
from domain.enums.estado_movimiento import (
    EstadoMovimiento,
)


class FakeCuentaRepository:

    def buscar_por_id(
        self,
        id_,
    ):
        return Cuenta(
            id=id_,
            empresa_id=1,
            codigo=f"{id_}",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )


def test_listar_devuelve_lista_de_movimientos(
    tmp_path,
):

    storage = Storage(
        tmp_path / "movimientos.json",
    )

    storage.save(
        [
            {
                "id": 1,
                "fecha": "2026-07-01",
                "descripcion": "Compra",
                "estado": "BORRADOR",
                "lineas": [
                    {
                        "cuenta_id": 10,
                        "importe": "1500.50",
                        "tipo_afectacion": "DEBITO",
                    }
                ],
            }
        ]
    )

    repository = MovimientoRepositoryJson(
        storage,
        FakeCuentaRepository(),
    )

    movimientos = repository.listar()

    assert len(movimientos) == 1

    assert isinstance(
        movimientos[0],
        Movimiento,
    )

    assert movimientos[0].id == 1

    assert movimientos[0].descripcion == "Compra"

    assert (
        movimientos[0].estado
        == EstadoMovimiento.BORRADOR
    )

    assert len(
        movimientos[0].lineas
    ) == 1

    assert (
        movimientos[0].lineas[0].cuenta.id
        == 10
    )

    assert (
        movimientos[0].lineas[0].importe
        == Decimal("1500.50")
    )

def test_buscar_por_id_devuelve_movimiento(
    tmp_path,
):

    storage = Storage(
        tmp_path / "movimientos.json",
    )

    storage.save(
        [
            {
                "id": 1,
                "fecha": "2026-07-01",
                "descripcion": "Compra",
                "estado": "BORRADOR",
                "lineas": [
                    {
                        "cuenta_id": 10,
                        "importe": "1500.50",
                        "tipo_afectacion": "DEBITO",
                    }
                ],
            }
        ]
    )

    repository = MovimientoRepositoryJson(
        storage,
        FakeCuentaRepository(),
    )

    movimiento = repository.buscar_por_id(
        1,
    )

    assert movimiento is not None

    assert movimiento.id == 1

    assert movimiento.descripcion == "Compra"

    assert (
        movimiento.estado
        == EstadoMovimiento.BORRADOR
    )

    assert len(
        movimiento.lineas
    ) == 1

    assert (
        movimiento.lineas[0].cuenta.id
        == 10
    )

def test_buscar_por_id_devuelve_none_si_no_existe(
    tmp_path,
):

    storage = Storage(
        tmp_path / "movimientos.json",
    )

    storage.save(
        [
            {
                "id": 1,
                "fecha": "2026-07-01",
                "descripcion": "Compra",
                "estado": "BORRADOR",
                "lineas": [
                    {
                        "cuenta_id": 10,
                        "importe": "1500.50",
                        "tipo_afectacion": "DEBITO",
                    }
                ],
            }
        ]
    )

    repository = MovimientoRepositoryJson(
        storage,
        FakeCuentaRepository(),
    )

    movimiento = repository.buscar_por_id(
        999,
    )

    assert movimiento is None

from decimal import Decimal

from domain.entities.linea_movimiento import (
    LineaMovimiento,
)

from domain.entities.movimiento import (
    Movimiento,
)

from domain.enums.estado_movimiento import (
    EstadoMovimiento,
)

from domain.enums.tipo_afectacion import (
    TipoAfectacion,
)

from domain.entities.cuenta import (
    Cuenta,
)

from domain.enums.tipo_cuenta import (
    TipoCuenta,
)


def test_guardar_agrega_un_movimiento(
    tmp_path,
):

    storage = Storage(
        tmp_path / "movimientos.json",
    )

    repository = MovimientoRepositoryJson(
        storage,
        FakeCuentaRepository(),
    )

    cuenta = Cuenta(
        id=10,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    linea = LineaMovimiento(
        cuenta=cuenta,
        importe=Decimal("1500.50"),
        tipo_afectacion=TipoAfectacion.DEBITO,
    )

    movimiento = Movimiento(
        id=1,
        fecha=date(2026, 7, 1),
        descripcion="Compra",
        estado=EstadoMovimiento.BORRADOR,
        lineas=[
            linea,
        ],
    )

    repository.guardar(
        movimiento,
    )

    movimientos = repository.listar()

    assert len(
        movimientos
    ) == 1

    assert movimientos[0].id == 1

    assert (
        movimientos[0].descripcion
        == "Compra"
    )

    assert len(
        movimientos[0].lineas
    ) == 1

    assert (
        movimientos[0].lineas[0].cuenta.id
        == 10
    )

    assert (
        movimientos[0].lineas[0].importe
        == Decimal("1500.50")
    )
def test_guardar_actualiza_si_el_id_ya_existe(
    tmp_path,
):

    storage = Storage(
        tmp_path / "movimientos.json",
    )

    repository = MovimientoRepositoryJson(
        storage,
        FakeCuentaRepository(),
    )

    cuenta = Cuenta(
        id=10,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    linea = LineaMovimiento(
        cuenta=cuenta,
        importe=Decimal("1500.50"),
        tipo_afectacion=TipoAfectacion.DEBITO,
    )

    repository.guardar(
        Movimiento(
            id=1,
            fecha=date(2026, 7, 1),
            descripcion="Compra",
            estado=EstadoMovimiento.BORRADOR,
            lineas=[linea],
        )
    )

    repository.guardar(
        Movimiento(
            id=1,
            fecha=date(2026, 7, 1),
            descripcion="Compra Actualizada",
            estado=EstadoMovimiento.BORRADOR,
            lineas=[linea],
        )
    )

    movimientos = repository.listar()

    assert len(movimientos) == 1

    assert movimientos[0].id == 1

    assert (
        movimientos[0].descripcion
        == "Compra Actualizada"
    )

def test_eliminar_quita_el_movimiento(
    tmp_path,
):

    storage = Storage(
        tmp_path / "movimientos.json",
    )

    repository = MovimientoRepositoryJson(
        storage,
        FakeCuentaRepository(),
    )

    cuenta = Cuenta(
        id=10,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    linea = LineaMovimiento(
        cuenta=cuenta,
        importe=Decimal("1500.50"),
        tipo_afectacion=TipoAfectacion.DEBITO,
    )

    movimiento = Movimiento(
        id=1,
        fecha=date(2026, 7, 1),
        descripcion="Compra",
        estado=EstadoMovimiento.BORRADOR,
        lineas=[linea],
    )

    repository.guardar(
        movimiento,
    )

    repository.eliminar(
        1,
    )

    movimientos = repository.listar()

    assert len(movimientos) == 0

def test_eliminar_id_inexistente_no_hace_nada(
    tmp_path,
):

    storage = Storage(
        tmp_path / "movimientos.json",
    )

    repository = MovimientoRepositoryJson(
        storage,
        FakeCuentaRepository(),
    )

    cuenta = Cuenta(
        id=10,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    linea = LineaMovimiento(
        cuenta=cuenta,
        importe=Decimal("1500.50"),
        tipo_afectacion=TipoAfectacion.DEBITO,
    )

    movimiento = Movimiento(
        id=1,
        fecha=date(2026, 7, 1),
        descripcion="Compra",
        estado=EstadoMovimiento.BORRADOR,
        lineas=[linea],
    )

    repository.guardar(
        movimiento,
    )

    repository.eliminar(
        999,
    )

    movimientos = repository.listar()

    assert len(movimientos) == 1

    assert movimientos[0].id == 1

    assert (
        movimientos[0].descripcion
        == "Compra"
    )


