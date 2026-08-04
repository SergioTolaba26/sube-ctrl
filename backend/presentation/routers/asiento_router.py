from pathlib import Path

from fastapi import APIRouter
from fastapi import HTTPException

from persistence.json_storage import JsonStorage

from infrastructure.repositories.json.movimiento_repository import (
    MovimientoRepositoryJson,
)
from infrastructure.repositories.json.cuenta_repository import (
    CuentaRepositoryJson,
)
from infrastructure.repositories.json.ejercicio_repository import (
    EjercicioRepositoryJson,
)

from domain.services.movimiento_service import (
    MovimientoService,
)
from domain.services.cuenta_service import (
    CuentaService,
)
from domain.services.ejercicio_service import (
    EjercicioService,
)

from application.use_cases.movimiento.listar_asientos import (
    ListarAsientos,
)
from application.use_cases.movimiento.buscar_asiento import (
    BuscarAsiento,
)
from application.use_cases.movimiento.registrar_asiento_contable import (
    RegistrarAsientoContable,
)
from application.use_cases.movimiento.confirmar_asiento import (
    ConfirmarAsiento,
)
from application.use_cases.movimiento.modificar_asiento import (
    ModificarAsiento,
)
from application.use_cases.movimiento.eliminar_asiento import (
    EliminarAsiento,
)

from presentation.schemas.movimiento_schema import (
    MovimientoResponse,
)
from presentation.schemas.registrar_asiento_request import (
    RegistrarAsientoRequest,
)

from presentation.mappers.movimiento_response_mapper import (
    MovimientoResponseMapper,
)

router = APIRouter(
    prefix="/asientos",
    tags=["Asientos"],
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


@router.get(
    "/",
    response_model=list[
        MovimientoResponse
    ],
)
def listar():

    use_case = ListarAsientos(
        service_movimientos,
    )

    movimientos = use_case.execute()

    return [
        MovimientoResponseMapper.to_resumen(
            movimiento,
        )
        for movimiento in movimientos
    ]


@router.get(
    "/{movimiento_id}",
    response_model=MovimientoResponse,
)
def buscar(
    movimiento_id: int,
):

    use_case = BuscarAsiento(
        service_movimientos,
    )

    movimiento = use_case.execute(
        movimiento_id,
    )

    if movimiento is None:

        raise HTTPException(
            status_code=404,
            detail="Asiento no encontrado.",
        )

    return MovimientoResponseMapper.to_detalle(
        movimiento,
    )


@router.post("/")
def registrar_asiento(
    request: RegistrarAsientoRequest,
):

    use_case = RegistrarAsientoContable(
        service_movimientos,
        service_cuentas,
        service_ejercicios,
    )

    try:

        movimiento = use_case.execute(
            fecha=request.fecha,
            descripcion=request.descripcion,
            lineas=[
                linea.model_dump()
                for linea in request.lineas
            ],
        )

        return {
            "mensaje": "Asiento creado en estado BORRADOR.",
            "movimiento": {
                "id": movimiento.id,
                "fecha": movimiento.fecha,
                "descripcion": movimiento.descripcion,
                "estado": movimiento.estado,
                "cantidad_lineas": len(
                    movimiento.lineas
                ),
            },
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.post(
    "/{movimiento_id}/confirmar",
)
def confirmar(
    movimiento_id: int,
):

    use_case = ConfirmarAsiento(
        service_movimientos,
    )

    try:

        movimiento = use_case.execute(
            movimiento_id,
        )

        return {
            "mensaje": "Asiento confirmado correctamente.",
            "movimiento": {
                "id": movimiento.id,
                "estado": movimiento.estado,
            },
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.put(
    "/{movimiento_id}",
)
def modificar_asiento(
    movimiento_id: int,
    request: RegistrarAsientoRequest,
):

    use_case = ModificarAsiento(
        service_movimientos,
        service_cuentas,
    )

    try:

        movimiento = use_case.execute(
            movimiento_id=movimiento_id,
            fecha=request.fecha,
            descripcion=request.descripcion,
            lineas=[
                linea.model_dump()
                for linea in request.lineas
            ],
        )

        return {
            "mensaje": "Asiento modificado correctamente.",
            "movimiento": {
                "id": movimiento.id,
                "fecha": movimiento.fecha,
                "descripcion": movimiento.descripcion,
                "estado": movimiento.estado,
                "cantidad_lineas": len(
                    movimiento.lineas
                ),
            },
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.delete(
    "/{movimiento_id}",
)
def eliminar_asiento(
    movimiento_id: int,
):

    use_case = EliminarAsiento(
        service_movimientos,
    )

    try:

        use_case.execute(
            movimiento_id,
        )

        return {
            "mensaje": "Asiento eliminado correctamente."
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )