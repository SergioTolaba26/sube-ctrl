
from pathlib import Path

from fastapi import APIRouter
from fastapi import HTTPException


from persistence.json_storage import JsonStorage

from infrastructure.repositories.json.ejercicio_repository import (
    EjercicioRepositoryJson,
)

from domain.services.ejercicio_service import (
    EjercicioService,
)

from infrastructure.repositories.json.movimiento_repository import (
    MovimientoRepositoryJson,
)

from domain.services.movimiento_service import (
    MovimientoService,
)

from infrastructure.repositories.json.cuenta_repository import (
    CuentaRepositoryJson,
)

from domain.services.cuenta_service import (
    CuentaService,
)

from application.use_cases.ejercicio.listar_ejercicios_use_case import (
    ListarEjercicios,
)

from application.use_cases.ejercicio.cerrar_ejercicio_use_case import (
    CerrarEjercicio,
)
from presentation.schemas.ejercicio_schema import (
    EjercicioResponse,
)
from application.factory import (
    ApplicationFactory,
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
# Ejercicios
#
storage_ejercicios = JsonStorage(
    Path("data/ejercicios.json"),
)

repository_ejercicios = EjercicioRepositoryJson(
    storage_ejercicios,
)

service_ejercicios = EjercicioService(
    repository_ejercicios,
)
#
# Cuentas
#
storage_cuentas = JsonStorage(
    Path("data/cuentas.json"),
)

repository_cuentas = CuentaRepositoryJson(
    storage_cuentas,
)

service_cuentas = CuentaService(
    repository_cuentas,
)

#
# Movimientos
#
storage_movimientos = JsonStorage(
    Path("data/movimientos.json"),
)


repository_movimientos = MovimientoRepositoryJson(
    storage_movimientos,
    repository_cuentas,
)

service_movimientos = MovimientoService(
    repository_movimientos,
)



@router.get("/")
def listar():

    use_case = ListarEjercicios(
        service_ejercicios,
    )

    return use_case.execute()

@router.post("/")
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

@router.post("/{ejercicio_id}/cerrar")
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