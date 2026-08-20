from domain.services.cuenta_service import (
    CuentaService,
)
from tests.factories.cuenta_factory import (
    CuentaFactory,
)

class FakeCuentaRepository:

    def listar(
        self,
        empresa_id,
    ):
        self.empresa_id_recibido = empresa_id
        return [
            CuentaFactory.crear(
                id=1,
                codigo="1.1.01",
                nombre="Caja",
            ),
            CuentaFactory.crear(
                id=2,
                codigo="1.1.02",
                nombre="Banco",
            ),
        ]

    def buscar_por_id(
        self,
        empresa_id,
        cuenta_id,
    ):
        self.empresa_id_recibido = empresa_id
        self.id_recibido = cuenta_id

        return f"cuenta-{empresa_id}-{cuenta_id}"
    def buscar_por_codigo(
        self,
        empresa_id,
        codigo,
    ):
        self.empresa_id_recibido = empresa_id
        self.codigo_recibido = codigo

        return f"cuenta-{empresa_id}-{codigo}"
    def guardar(
        self,
        cuenta,
    ):
        self.cuenta_guardada = cuenta
    def eliminar(
        self,
        empresa_id,
        cuenta_id,
    ):
        self.empresa_id_eliminado = empresa_id
        self.id_eliminado = cuenta_id

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

    cuentas = service.listar(
        1,
    )

    assert (
        repository.empresa_id_recibido
        == 1
    )

    assert len(cuentas) == 2

    assert cuentas[0].codigo == "1.1.01"

    assert cuentas[1].codigo == "1.1.02"
def test_buscar_por_id():

    repository = FakeCuentaRepository()

    service = CuentaService(
        repository,
    )

    cuenta = service.buscar_por_id(
        1,
        10,
    )

    assert (
        repository.empresa_id_recibido
        == 1
    )

    assert (
        repository.id_recibido
        == 10
    )

    assert cuenta == "cuenta-1-10"
def test_buscar_por_codigo():

    repository = FakeCuentaRepository()

    service = CuentaService(
        repository,
    )

    cuenta = service.buscar_por_codigo(
        1,
        "1.1.01",
    )

    assert (
        repository.empresa_id_recibido
        == 1
    )

    assert (
        repository.codigo_recibido
        == "1.1.01"
    )

    assert cuenta == "cuenta-1-1.1.01"
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
        1,
        15,
    )

    assert (
        repository.empresa_id_eliminado
        == 1
    )

    assert (
        repository.id_eliminado
        == 15
    )