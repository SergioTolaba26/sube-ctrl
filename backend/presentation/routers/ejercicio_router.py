from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from presentation.dependencies import (
    get_application_factory,
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


@router.get(
    "/",
)
def listar(
    empresa_id: int,
    factory: ApplicationFactory = Depends(
        get_application_factory,
    ),
):

    use_case = ListarEjercicios(
        factory.ejercicio_service,
    )

    return use_case.execute(
        empresa_id,
    )

@router.get(
    "/{ejercicio_id}",
    response_model=EjercicioResponse,
)
def buscar_ejercicio(
    ejercicio_id: int,
    empresa_id: int,
    factory: ApplicationFactory = Depends(
        get_application_factory,
    ),
):

    use_case = factory.buscar_ejercicio()

    ejercicio = use_case.execute(
        empresa_id,
        ejercicio_id,
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
    empresa_id: int,
    factory: ApplicationFactory = Depends(
        get_application_factory,
    ),
):

    use_case = factory.registrar_ejercicio()

    try:

        ejercicio = use_case.execute(

            empresa_id=empresa_id,

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
    empresa_id: int,
    request: RegistrarEjercicioRequest,
    factory: ApplicationFactory = Depends(
        get_application_factory,
    ),
):
    use_case = ModificarEjercicio(
        factory.ejercicio_service,
    )

    try:

        return use_case.execute(
            empresa_id=empresa_id,
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
    empresa_id: int,
    factory: ApplicationFactory = Depends(
        get_application_factory,
    ),
):
    use_case = EliminarEjercicio(
        factory.ejercicio_service,
    )

    try:

        use_case.execute(
            empresa_id,
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

    factory: ApplicationFactory = Depends(
        get_application_factory,
    ),

):

    use_case = CerrarEjercicio(

        factory.ejercicio_repository,

        factory.movimiento_service,

        factory.cuenta_service,

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