from domain.entities.ejercicio_contable import EjercicioContable


def mostrar_ejercicio(
    ejercicio: EjercicioContable,
) -> None:

    print()
    print("=" * 40)
    print(" DEMO - CIERRE DE EJERCICIO")
    print("=" * 40)
    print()

    print("Ejercicio Contable")
    print("------------------")
    print(
        f"Desde : {ejercicio.fecha_inicio:%d/%m/%Y}"
    )
    print(
        f"Hasta : {ejercicio.fecha_fin:%d/%m/%Y}"
    )
    print(
        f"Estado: {ejercicio.estado.value}"
    )