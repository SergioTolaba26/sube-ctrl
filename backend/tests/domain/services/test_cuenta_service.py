from domain.services.cuenta_service import (
    CuentaService,
)
from tests.factories.cuenta_factory import (
    CuentaFactory,
)

class FakeCuentaRepository:

    def listar(
        self,
    ):
        return [
            "cuenta1",
            "cuenta2",
        ]

    def buscar_por_id(
        self,
        id_,
    ):
        self.id_recibido = id_

        return f"cuenta-{id_}"
    def buscar_por_codigo(
        self,
        codigo,
    ):
        self.codigo_recibido = codigo

        return f"cuenta-{codigo}"
    def guardar(
        self,
        cuenta,
    ):
        self.cuenta_guardada = cuenta
    def eliminar(
        self,
        id_,
    ):
        self.id_eliminado = id_

def test_crea_service():

    repository = FakeCuentaRepository()

    service = CuentaService(
        repository,
    )

    assert (
        service.repository
        is repository
    )

def test_listar():

    repository = FakeCuentaRepository()

    service = CuentaService(
        repository,
    )

    cuentas = service.listar()

    assert cuentas == [
        "cuenta1",
        "cuenta2",
    ]

def test_buscar_por_id():

    repository = FakeCuentaRepository()

    service = CuentaService(
        repository,
    )

    cuenta = service.buscar_por_id(
        10,
    )

    assert (
        repository.id_recibido
        == 10
    )

    assert cuenta == "cuenta-10"

def test_buscar_por_codigo():

    repository = FakeCuentaRepository()

    service = CuentaService(
        repository,
    )

    cuenta = service.buscar_por_codigo(
        "1.1.01",
    )

    assert (
        repository.codigo_recibido
        == "1.1.01"
    )

    assert cuenta == "cuenta-1.1.01"

from domain.entities.cuenta import (
    Cuenta,
)
from domain.enums.tipo_cuenta import (
    TipoCuenta,
)


def test_guardar():

    repository = FakeCuentaRepository()

    service = CuentaService(
        repository,
    )

    cuenta = CuentaFactory.crear()
    # si necesito cambiar algun dato
#     cuenta = CuentaFactory.crear(
#     id=10,
#     nombre="Banco Nación",
# )
    service.guardar(
        cuenta,
    )

    assert (
        repository.cuenta_guardada
        is cuenta
    )

def test_eliminar():

    repository = FakeCuentaRepository()

    service = CuentaService(
        repository,
    )

    service.eliminar(
        15,
    )

    assert (
        repository.id_eliminado
        == 15
    )