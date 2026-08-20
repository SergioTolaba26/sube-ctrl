from dotenv import load_dotenv

load_dotenv()


from infrastructure.postgres.database import (
    DatabasePostgres,
)

from infrastructure.postgres.empresa_repository import (
    EmpresaRepositoryPostgres,
)

from domain.entities.empresa import Empresa


database = DatabasePostgres()

repository = EmpresaRepositoryPostgres(
    database.connection,
)


empresa = Empresa(
    id=1,
    razon_social="Empresa PostgreSQL Prueba",
    nombre_fantasia="Empresa PG",
    cuit="30712345678",
)


repository.guardar(
    empresa,
)


print(
    "GUARDADA:",
    empresa,
)


empresas = repository.listar()


print(
    "LISTADAS:",
    empresas,
)


encontrada = repository.buscar_por_id(
    1,
)


print(
    "BUSCADA:",
    encontrada,
)