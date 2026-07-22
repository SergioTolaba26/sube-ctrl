"""
Dependencias compartidas de la API.

En este módulo se construirán los objetos
que utilizarán los routers:

Storage
Repository
Service
UseCase
"""

from typing import Protocol

from application.use_cases.empresa.registrar_empresa import (
    RegistrarEmpresa,
)
#from persistence.storage import Storage

from infrastructure.repositories.json.empresa_repository import (
    EmpresaRepositoryJson,
)

from domain.services.empresa_service import (
    EmpresaService,
)

from application.use_cases.empresa.registrar_empresa import (
    RegistrarEmpresa,
)

class EmpresaDependencies(Protocol):

    def registrar_empresa(
        self,
    ) -> RegistrarEmpresa:
        ...