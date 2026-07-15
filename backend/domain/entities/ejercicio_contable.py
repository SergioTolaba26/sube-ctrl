from dataclasses import dataclass, field
from datetime import date

from domain.enums.estado_ejercicio import EstadoEjercicio
from datetime import date



@dataclass(slots=True)
class EjercicioContable:

    id: int | None

    empresa_id: int # multiempresa

    fecha_inicio: date
    fecha_fin: date

    estado: EstadoEjercicio = field(
        default=EstadoEjercicio.ABIERTO
    )

    def esta_abierto(self) -> bool:
        return self.estado == EstadoEjercicio.ABIERTO
    
   

    def esta_cerrado(self) -> bool:
        return self.estado == EstadoEjercicio.CERRADO
    
    def cerrar(self) -> None:

        if self.esta_cerrado():
            raise ValueError(
                "El ejercicio ya está cerrado."
            )

        self.estado = EstadoEjercicio.CERRADO



    def contiene(self, fecha: date) -> bool:
        return self.fecha_inicio <= fecha <= self.fecha_fin
    
    def __post_init__(self):
        if self.fecha_inicio > self.fecha_fin:
            raise ValueError(
                "La fecha de inicio debe ser anterior a la fecha de fin."
            )