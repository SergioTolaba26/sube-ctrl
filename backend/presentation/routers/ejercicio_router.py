from pathlib import Path

from fastapi import APIRouter
from fastapi import HTTPException

from persistence.json_storage import JsonStorage

from infrastructure.postgres.database import (
    DatabasePostgres,
)

from infrastructure.postgres.ejercicio_repository import (
    EjercicioRepositoryPostgres,
)

from infrastructure.repositories.json.movimiento_repository import (
    MovimientoRepositoryJson,
)

from infrastructure.repositories.json.cuenta_repository import (
    CuentaRepositoryJson,
)

from domain.services.ejercicio_service import (
    EjercicioService,
)

from domain.services.movimiento_service import (
    MovimientoService,
)

from domain.services.cuenta_service import (
    CuentaService,
)

from application.factory import (
    ApplicationFactory,
)

from application.use_cases.ejercicio.listar_ejercicios_use_case import (
    ListarEjercicios,
)

from application.use_cases.ejercicio.cerrar_ejercicio_use_case import (
    CerrarEjercicio,
)

from application.use_cases.ejercicio.modificar_ejercicio import (
    ModificarEjercicio,
)

from application.use_cases.ejercicio.eliminar_ejercicio import (
    EliminarEjercicio,
)

from presentation.schemas.ejercicio_schema import (
    EjercicioResponse,
)

from presentation.schemas.registrar_ejercicio_request import (
    RegistrarEjercicioRequest,
)

router = APIRouter(
    prefix="/ejercicios",
    tags=["Ejercicios"],
)

factory = ApplicationFactory()

#
# Storage
#

storage_ejercicios = JsonStorage(
    Path("data/ejercicios.json"),
)

storage_cuentas = JsonStorage(
    Path("data/cuentas.json"),
)

storage_movimientos = JsonStorage(
    Path("data/movimientos.json"),
)

#
# Repositories
#

database = DatabasePostgres()

repository_ejercicios = EjercicioRepositoryPostgres(
    database.connection,
)

repository_cuentas = CuentaRepositoryJson(
    storage_cuentas,
)

repository_movimientos = MovimientoRepositoryJson(
    storage_movimientos,
    repository_cuentas,
)

#
# Services
#

service_ejercicios = EjercicioService(
    repository_ejercicios,
)

service_cuentas = CuentaService(
    repository_cuentas,
)

service_movimientos = MovimientoService(
    repository_movimientos,
)

#
# Endpoints
#

@router.get(
    "/",
)
def listar():

    use_case = ListarEjercicios(
        service_ejercicios,
    )

    return use_case.execute()


@router.get(
    "/{id}",
    response_model=EjercicioResponse,
)
def buscar_ejercicio(
    id: int,
):

    use_case = factory.buscar_ejercicio()

    ejercicio = use_case.execute(
        id,
    )

    if ejercicio is None:

        raise HTTPException(
            status_code=404,
            detail="Ejercicio no encontrado.",
        )

    return ejercicio


@router.post(
    "/",
)
def registrar(
    request: RegistrarEjercicioRequest,
):

    use_case = factory.registrar_ejercicio()

    try:

        ejercicio = use_case.execute(

            anio=request.anio,

            fecha_apertura=request.fecha_apertura,

            fecha_cierre=request.fecha_cierre,

        )

        return {

            "mensaje": "Ejercicio creado correctamente.",

            "ejercicio": ejercicio,

        }

    except ValueError as error:

        raise HTTPException(

            status_code=400,

            detail=str(error),

        )


@router.put(
    "/{ejercicio_id}",
    response_model=EjercicioResponse,
)
def actualizar(

    ejercicio_id: int,

    request: RegistrarEjercicioRequest,

):

    use_case = ModificarEjercicio(
        service_ejercicios,
    )

    try:

        return use_case.execute(

            ejercicio_id=ejercicio_id,

            anio=request.anio,

            fecha_apertura=request.fecha_apertura,

            fecha_cierre=request.fecha_cierre,

        )

    except ValueError as error:

        raise HTTPException(

            status_code=400,

            detail=str(error),

        )


@router.delete(
    "/{ejercicio_id}",
)
def eliminar(
    ejercicio_id: int,
):

    use_case = EliminarEjercicio(
        service_ejercicios,
    )

    try:

        use_case.execute(
            ejercicio_id,
        )

        return {

            "mensaje": "Ejercicio eliminado correctamente.",

        }

    except ValueError as error:

        raise HTTPException(

            status_code=400,

            detail=str(error),

        )


@router.post(
    "/{ejercicio_id}/cerrar",
)
def cerrar(
    ejercicio_id: int,
):

    use_case = CerrarEjercicio(

        repository_ejercicios,

        service_movimientos,

        service_cuentas,

    )

    try:

        ejercicio = use_case.execute(
            ejercicio_id,
        )

        return {

            "mensaje": "Ejercicio cerrado correctamente.",

            "ejercicio": ejercicio,

        }

    except ValueError as error:

        raise HTTPException(

            status_code=400,

            detail=str(error),

        )