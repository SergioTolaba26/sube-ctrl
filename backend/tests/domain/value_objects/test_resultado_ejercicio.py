from decimal import Decimal

from domain.enums.tipo_afectacion import TipoAfectacion
from domain.value_objects.resultado_ejercicio import ResultadoEjercicio


def test_un_resultado_positivo_genera_un_credito():
    """
    Una ganancia genera un crédito
    en la línea de contrapartida.
    """

    resultado = ResultadoEjercicio(
        importe=Decimal("700"),
    )

    linea = resultado.generar_linea_de_cierre()

    assert linea.importe == Decimal("700")
    assert linea.tipo_afectacion == TipoAfectacion.CREDITO