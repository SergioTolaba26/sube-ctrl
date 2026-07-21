from domain.services.empresa_service import (
    EmpresaService,
)


class FakeEmpresaRepository:

    def listar(
        self,
    ):
        return [
            "empresa1",
            "empresa2",
        ]

    def buscar_por_id(
        self,
        id_,
    ):
        self.id_recibido = id_

        return f"empresa-{id_}"
    def guardar(
        self,
        empresa,
    ):
        self.empresa_guardada = empresa
    def eliminar(
        self,
        id_,
    ):
        self.id_eliminado = id_    

def test_crea_service():

    repository = FakeEmpresaRepository()

    service = EmpresaService(
        repository,
    )

    assert (
        service.repository
        is repository
    )

def test_listar_devuelve_empresas():

    repository = FakeEmpresaRepository()

    service = EmpresaService(
        repository,
    )

    empresas = service.listar()

    assert empresas == [
        "empresa1",
        "empresa2",
    ]

def test_buscar_por_id():

    repository = FakeEmpresaRepository()

    service = EmpresaService(
        repository,
    )

    empresa = service.buscar_por_id(
        7,
    )

    assert (
        repository.id_recibido
        == 7
    )

    assert empresa == "empresa-7"

from domain.entities.empresa import (
    Empresa,
)


from domain.entities.empresa import (
    Empresa,
)


def test_guardar():

    repository = FakeEmpresaRepository()

    service = EmpresaService(
        repository,
    )

    empresa = Empresa(
        id=1,
        razon_social="Mi Empresa S.A.",
        nombre_fantasia="Mi Empresa",
        cuit="30123456789",
    )

    service.guardar(
        empresa,
    )

    assert (
        repository.empresa_guardada
        is empresa
    )

def test_eliminar():

    repository = FakeEmpresaRepository()

    service = EmpresaService(
        repository,
    )

    service.eliminar(
        7,
    )

    assert (
        repository.id_eliminado
        == 7
    )