class ListarAsientos:

    def __init__(
        self,
        movimiento_service,
    ):
        self.movimiento_service = movimiento_service

    def execute(
        self,
    ):
        return self.movimiento_service.listar()