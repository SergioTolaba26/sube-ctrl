

from datetime import date

from domain.entities.ejercicio_contable import EjercicioContable
from demo.impresor import mostrar_ejercicio



ejercicio = EjercicioContable(
    id=None,
    fecha_inicio=date(2026, 1, 1),
    fecha_fin=date(2026, 12, 31),
)

#print(ejercicio)
mostrar_ejercicio(ejercicio)