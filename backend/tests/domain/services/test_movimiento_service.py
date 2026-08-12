from datetime import date

from domain.entities.movimiento import Movimiento
from domain.enums.estado_movimiento import EstadoMovimiento
from domain.services.movimiento_service import MovimientoService


class FakeMovimientoRepository:

    def listar(
        self,
    ):
        return [
            Movimiento(
                id=1,
                empresa_id=1,
                ejercicio_id=1,
                fecha=date(
                    2026,
                    7,
                    20,
                ),
                descripcion="Movimiento 1",
                estado=EstadoMovimiento.BORRADOR,
                lineas=[],
            ),
            Movimiento(
                id=2,
                empresa_id=1,
                ejercicio_id=1,
                fecha=date(
                    2026,
                    7,
                    21,
                ),
                descripcion="Movimiento 2",
                estado=EstadoMovimiento.BORRADOR,
                lineas=[],
            ),
        ]

    def buscar_por_id(
        self,
        id_,
    ):
        self.id_recibido = id_

        return f"movimiento-{id_}"

    def guardar(
        self,
        movimiento,
    ):
        self.movimiento_guardado = movimiento

    def eliminar(
        self,
        id_,
    ):
        self.id_eliminado = id_


def test_crea_service():

    repository = FakeMovimientoRepository()

    service = MovimientoService(
        repository,
    )

    assert (
        service.repository
        is repository
    )


def test_listar():

    repository = FakeMovimientoRepository()

    service = MovimientoService(
        repository,
    )

    movimientos = service.listar()

    assert len(
        movimientos,
    ) == 2

    assert movimientos[0].id == 1

    assert movimientos[1].id == 2


def test_buscar_por_id():

    repository = FakeMovimientoRepository()

    service = MovimientoService(
        repository,
    )

    movimiento = service.buscar_por_id(
        25,
    )

    assert (
        repository.id_recibido
        == 25
    )

    assert movimiento == "movimiento-25"


def test_guardar():

    repository = FakeMovimientoRepository()

    service = MovimientoService(
        repository,
    )

    movimiento = Movimiento(
        id=1,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(
            2026,
            7,
            20,
        ),
        descripcion="Compra de mercadería",
        estado=EstadoMovimiento.BORRADOR,
        lineas=[],
    )

    service.guardar(
        movimiento,
    )

    assert (
        repository.movimiento_guardado
        is movimiento
    )


def test_eliminar():

    repository = FakeMovimientoRepository()

    service = MovimientoService(
        repository,
    )

    service.eliminar(
        25,
    )

    assert (
        repository.id_eliminado
        == 25
    )