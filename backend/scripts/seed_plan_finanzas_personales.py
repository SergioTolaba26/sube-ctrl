
"""
Carga el plan de cuentas de Finanzas Personales
para una empresa determinada utilizando PostgreSQL
y los casos de uso de la aplicación.
"""

from pathlib import Path
import sys


BASE_DIR = Path(
    __file__
).resolve().parent.parent

sys.path.insert(
    0,
    str(BASE_DIR),
)


from application.container import (
    ApplicationContainer,
)

from data.planes.plan_finanzas_personales import (
    PLAN_FINANZAS_PERSONALES,
)


EMPRESA_ID = 2


def main():

    container = ApplicationContainer()

    registrar_cuenta = (
        container.registrar_cuenta()
    )

    buscar_cuenta = (
        container.buscar_cuenta_por_codigo()
    )

    print(
        f"\nCargando plan de cuentas "
        f"para empresa {EMPRESA_ID}\n"
    )

    for cuenta in PLAN_FINANZAS_PERSONALES:

        existente = buscar_cuenta.execute(
            EMPRESA_ID,
            cuenta["codigo"],
        )

        if existente is not None:

            print(
                f"[YA EXISTE] "
                f"{cuenta['codigo']} - "
                f"{cuenta['nombre']}"
            )

            continue

        try:

            cuenta_creada = (
                registrar_cuenta.execute(
                    empresa_id=EMPRESA_ID,
                    codigo=cuenta["codigo"],
                    nombre=cuenta["nombre"],
                    tipo=cuenta["tipo"],
                    imputable=cuenta["imputable"],
                )
            )

            print(
                f"[CREADA] "
                f"ID={cuenta_creada.id} - "
                f"{cuenta_creada.codigo} - "
                f"{cuenta_creada.nombre}"
            )

        except Exception as e:

            print(
                f"[ERROR] "
                f"{cuenta['codigo']} - {e}"
            )


if __name__ == "__main__":

    main()

