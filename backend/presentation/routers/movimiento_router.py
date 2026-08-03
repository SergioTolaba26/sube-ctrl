from pathlib import Path

from fastapi import APIRouter

from persistence.json_storage import JsonStorage

from infrastructure.repositories.json.cuenta_repository import (
    CuentaRepositoryJson,
)

from infrastructure.repositories.json.movimiento_repository import (
    MovimientoRepositoryJson,
)

from domain.services.movimiento_service import (
    MovimientoService,
)


# Agregamos este import para GET/movimientos
from application.use_cases.movimiento.listar_movimientos import (
    ListarMovimientos,
)


from application.use_cases.movimiento.buscar_movimiento import (
    BuscarMovimiento,
)

from fastapi import HTTPException

from application.use_cases.movimiento.modificar_movimiento import (
    ModificarMovimiento,
)

from application.use_cases.movimiento.eliminar_movimiento import (
    EliminarMovimiento,
)
# Linea movimiento
from presentation.schemas.linea_movimiento_schema import (
    LineaMovimientoCreate,
    LineaMovimientoResponse,
)

from application.use_cases.movimiento.agregar_linea_movimiento import (
    AgregarLineaMovimiento,
)

from domain.services.cuenta_service import (
    CuentaService,
)
# Agregar linea movimiento
from fastapi import HTTPException

from application.use_cases.movimiento.agregar_linea_movimiento import (
    AgregarLineaMovimiento,
)

from application.use_cases.movimiento.modificar_linea_movimiento import (
    ModificarLineaMovimiento,
)

from application.use_cases.movimiento.eliminar_linea_movimiento import (
    EliminarLineaMovimiento,
)

from domain.services.cuenta_service import (
    CuentaService,
)

from presentation.schemas.linea_movimiento_schema import (
    LineaMovimientoCreate,
    LineaMovimientoResponse,
)

from application.use_cases.movimiento.confirmar_movimiento import (
    ConfirmarMovimiento,
)

from application.factory import (
    ApplicationFactory,
)
from presentation.schemas.movimiento_resumen_response import MovimientoResumenResponse
from presentation.schemas.registrar_asiento_request import (
    RegistrarAsientoRequest,
)

from application.use_cases.movimiento.registrar_asiento_contable import (
    RegistrarAsientoContable,
)

from presentation.schemas.movimiento_schema import (
    MovimientoResponse,
    MovimientoUpdate,
)
from presentation.mappers.movimiento_response_mapper import (
    MovimientoResponseMapper,
)
router = APIRouter(
    prefix="/movimientos",
    tags=["Movimientos"],
)
factory = ApplicationFactory()

@router.post(
    "/",
    response_model=MovimientoResponse,
)
def registrar_movimiento(
    request: RegistrarAsientoRequest,
):

    use_case = factory.registrar_asiento_contable()

    movimiento = use_case.execute(
        fecha=request.fecha,
        descripcion=request.descripcion,
        lineas=[
            linea.model_dump()
            for linea in request.lineas
        ],
    )

    return movimiento
# Lo nuevo para GET/movimientos - agrego este endpoint  

from presentation.mappers.movimiento_response_mapper import (
    MovimientoResponseMapper,
)

@router.get(
    "/",
    response_model=list[MovimientoResumenResponse],
)
def listar_movimientos():

    use_case = factory.listar_movimientos()

    movimientos = use_case.execute()

    return [
        MovimientoResponseMapper.to_resumen(m)
        for m in movimientos
    ]
@router.get(
    "/{movimiento_id}",
    response_model=MovimientoResponse,
)
def buscar_movimiento(
    movimiento_id: int,
):

    use_case = factory.buscar_movimiento()

    movimiento = use_case.execute(
        movimiento_id,
    )

    if movimiento is None:

        raise HTTPException(
            status_code=404,
            detail="Movimiento inexistente.",
        )

    return {
        "id": movimiento.id,
        "numero_asiento": movimiento.numero_asiento,
        "fecha": movimiento.fecha,
        "descripcion": movimiento.descripcion,
        "estado": movimiento.estado,
        "lineas": [
            {
                "cuenta_id": linea.cuenta.id,
                "cuenta_codigo": linea.cuenta.codigo,
                "cuenta_nombre": linea.cuenta.nombre,
                "importe": linea.importe,
                "tipo_afectacion": linea.tipo_afectacion,
            }
            for linea in movimiento.lineas
        ],
    }
@router.put(
    "/{movimiento_id}",
    response_model=MovimientoResponse,
)
def modificar_movimiento(
    movimiento_id: int,
    movimiento: MovimientoUpdate,
):

    use_case = factory.modificar_movimiento()

    try:

        movimiento_modificado = use_case.execute(
            movimiento_id=movimiento_id,
            fecha=movimiento.fecha,
            descripcion=movimiento.descripcion,
            estado=movimiento.estado,
            lineas=movimiento.lineas,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    if movimiento_modificado is None:

        raise HTTPException(
            status_code=404,
            detail="Movimiento inexistente.",
        )

    # return movimiento_modificado
    return MovimientoResponseMapper.to_detalle(
    movimiento_modificado,
)
@router.delete(
    "/{movimiento_id}",
)
def eliminar_movimiento(
    movimiento_id: int,
):

    use_case = factory.eliminar_movimiento()

    try:

        eliminado = use_case.execute(
            movimiento_id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    if eliminado is None:

        raise HTTPException(
            status_code=404,
            detail="Movimiento inexistente.",
        )

    return {
        "mensaje": "Movimiento eliminado correctamente.",
    }

@router.post(
    "/{movimiento_id}/lineas",
    response_model=LineaMovimientoResponse,
)
def agregar_linea_movimiento(
    movimiento_id: int,
    linea: LineaMovimientoCreate,
):

    use_case = factory.agregar_linea_movimiento()

    try:

        linea_creada = use_case.execute(
            movimiento_id=movimiento_id,
            cuenta_id=linea.cuenta_id,
            importe=linea.importe,
            tipo_afectacion=linea.tipo_afectacion,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    if linea_creada is None:

        raise HTTPException(
            status_code=404,
            detail="Movimiento inexistente.",
        )

    return {
    "cuenta_id": linea_creada.cuenta.id,
    "cuenta_codigo": linea_creada.cuenta.codigo,
    "cuenta_nombre": linea_creada.cuenta.nombre,
    "importe": linea_creada.importe,
    "tipo_afectacion": linea_creada.tipo_afectacion,
}


@router.post(
    "/{movimiento_id}/confirmar",
)
def confirmar_movimiento(
    movimiento_id: int,
):

    cuenta_storage = JsonStorage(
        Path("data/cuentas.json")
    )

    cuenta_repository = CuentaRepositoryJson(
        cuenta_storage,
    )

    movimiento_storage = JsonStorage(
        Path("data/movimientos.json")
    )

    movimiento_repository = MovimientoRepositoryJson(
        movimiento_storage,
        cuenta_repository,
    )

    movimiento_service = MovimientoService(
        movimiento_repository,
    )

    use_case = ConfirmarMovimiento(
        movimiento_service,
    )

    try:

        movimiento = use_case.execute(
            movimiento_id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    if movimiento is None:

        raise HTTPException(
            status_code=404,
            detail="Movimiento no encontrado",
        )

    return {
        "mensaje": "Movimiento confirmado correctamente.",
        "estado": movimiento.estado.name,
    }