from domain.repositories.movimiento_repository import MovimientoRepository
from domain.services.libro_mayor import LibroMayor
from domain.entities.cuenta import Cuenta


class ConsultarLibroMayor:

    def __init__(
        self,
        repository: MovimientoRepository,
    ):
        self.repository = repository

    def execute(
        self,
        cuenta: Cuenta,
    ):
        movimientos = self.repository.listar()

        libro = LibroMayor()

        return libro.obtener(
            cuenta=cuenta,
            movimientos=movimientos,
        )