"""
Carga el plan de cuentas utilizando
los casos de uso de la aplicación.
"""
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from application.factory import (
    ApplicationFactory,
)

from data.planes.plan_minimo import (
    PLAN_MINIMO,
)


def main():

    factory = ApplicationFactory()

    registrar_cuenta = factory.registrar_cuenta()

    buscar_cuenta = factory.buscar_cuenta_por_codigo()

    for cuenta in PLAN_MINIMO:

        existente = buscar_cuenta.execute(
            cuenta["codigo"],
        )

        if existente is not None:

            print(
                f"[YA EXISTE] {cuenta['codigo']} - {cuenta['nombre']}"
            )

            continue

        try:

            registrar_cuenta.execute(
                codigo=cuenta["codigo"],
                nombre=cuenta["nombre"],
                tipo=cuenta["tipo"],
                imputable=cuenta["imputable"],
            )

            print(
                f"[CREADA] {cuenta['codigo']} - {cuenta['nombre']}"
            )

        except Exception as e:

            print(
                f"[ERROR] {cuenta['codigo']} - {e}"
            )


if __name__ == "__main__":
    main()