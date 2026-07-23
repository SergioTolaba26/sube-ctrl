from tests.builders.entidades_builder import crear_ejercicio
from demo.impresor import mostrar_ejercicio
from decimal import Decimal

from domain.use_cases.registrar_venta import RegistrarVenta
from domain.use_cases.registrar_compra import RegistrarCompra
from domain.use_cases.registrar_gasto import RegistrarGasto
from domain.use_cases.registrar_pago import RegistrarPago
from domain.use_cases.registrar_cobro import RegistrarCobro

from tests.builders.entidades_builder import (
    crear_caja,
    crear_ejercicio,
    crear_ventas,
    crear_compras,
    crear_gastos,
    crear_proveedores,
    crear_clientes,
)
from domain.use_cases.consultar_estado_resultados import (
    ConsultarEstadoResultados,
)
from domain.use_cases.consultar_balance_sumas_saldos import (
    ConsultarBalanceSumasSaldos,
)
from domain.use_cases.consultar_balance_general import (
    ConsultarBalanceGeneral,
)
from domain.use_cases.consultar_libro_diario import (
    ConsultarLibroDiario,
)
from domain.use_cases.consultar_libro_mayor import (
    ConsultarLibroMayor,
)

def main():
    
    ejercicio = crear_ejercicio()
    caja = crear_caja()
    ventas = crear_ventas()
    compras = crear_compras()
    gastos = crear_gastos()
    proveedores = crear_proveedores()
    clientes = crear_clientes()

    print()

    print("===================================")
    print("        DEMO CONTABILIDAD")
    print("===================================")
    print()

    print("Ejercicio creado:")

    #print(ejercicio)
    mostrar_ejercicio(ejercicio)


    movimientos = []
# ---------------- Registraré una VENTA
    registrar_venta = RegistrarVenta()

    movimiento_venta =registrar_venta.ejecutar(
        caja=caja,
        ventas=ventas,
        importe=Decimal("1000"),
    )

    print()

    print("----------------------------------------")
    print("VENTA REGISTRADA")
    print("----------------------------------------")

    for linea in movimiento_venta.lineas:

        tipo = (
            "Debe"
            if linea.es_debito()
            else "Haber"
        )

        print(
            f"{tipo:6}"
            f"{linea.cuenta.nombre:25}"
            f"$ {linea.importe}"
        )
    movimientos.append(
    movimiento_venta
    )
    # ---------------- Registraré una COMPRA
    registrar_compra = RegistrarCompra()

    movimiento_compra = registrar_compra.ejecutar(
        caja=caja,
        compras=compras,
        importe=Decimal("500"),
    )
    print()

    print("----------------------------------------")
    print("COMPRA REGISTRADA")
    print("----------------------------------------")
    # este for se repite en cada registro, luego se refactorizará
    for linea in movimiento_compra.lineas:

        tipo = (
            "Debe"
            if linea.es_debito()
            else "Haber"
        )

        print(
            f"{tipo:6}"
            f"{linea.cuenta.nombre:25}"
            f"$ {linea.importe}"
        )
    movimientos.append(
    movimiento_compra
    )
    
    # ---------------- Registraré un GASTO
    registrar_gasto = RegistrarGasto()

    movimiento_gasto = registrar_gasto.ejecutar(
        caja=caja,
        gastos=gastos,
        importe=Decimal("300"),
    )
    print()

    print("----------------------------------------")
    print("GASTO REGISTRADO")
    print("----------------------------------------")

    for linea in movimiento_gasto.lineas:

        tipo = (
            "Debe"
            if linea.es_debito()
            else "Haber"
        )

        print(
            f"{tipo:6}"
            f"{linea.cuenta.nombre:25}"
            f"$ {linea.importe}"
        )
    movimientos.append(
    movimiento_gasto
    )
    # ---------------- Registraré un PAGO
    registrar_pago = RegistrarPago()

    movimiento_pago = registrar_pago.ejecutar(
    caja=caja,
    proveedores=proveedores,
    importe=Decimal("500"),
    )
    print()

    print("----------------------------------------")
    print("PAGO REGISTRADO")
    print("----------------------------------------")

    for linea in movimiento_pago.lineas:

        tipo = (
            "Debe"
            if linea.es_debito()
            else "Haber"
        )

        print(
            f"{tipo:6}"
            f"{linea.cuenta.nombre:25}"
            f"$ {linea.importe}"
        )
    movimientos.append(
    movimiento_pago
    )
    
    # ---------------- Registraré un COBRO
    registrar_cobro = RegistrarCobro()

    movimiento_cobro = registrar_cobro.ejecutar(
        caja=caja,
        clientes=clientes,
        importe=Decimal("800"),
    )
    print()

    print("----------------------------------------")
    print("COBRO REGISTRADO")
    print("----------------------------------------")

    for linea in movimiento_cobro.lineas:

        tipo = (
            "Debe"
            if linea.es_debito()
            else "Haber"
        )

        print(
            f"{tipo:6}"
            f"{linea.cuenta.nombre:25}"
            f"$ {linea.importe}"
        )

    movimientos.append(
    movimiento_cobro
    )
    #----------------- RESUMEN de lo que registramos
    print()

    print("----------------------------------------")
    print("RESUMEN")
    print("----------------------------------------")

    print(
        f"Movimientos registrados: {len(movimientos)}"
    )
# ******************** LIBRO DIARIO *******************
    print()

    print("----------------------------------------")
    print("LIBRO DIARIO")
    print("----------------------------------------")

    libro = (
        ConsultarLibroDiario()
        .ejecutar(
            movimientos=movimientos,
        )
    )
    # ----------------------
    for movimiento in libro:

        print()

        print(
            f"{movimiento.fecha:%d/%m/%Y}   "
            f"{movimiento.descripcion}"
        )

        for linea in movimiento.lineas:

            tipo = (
                "Debe"
                if linea.es_debito()
                else "Haber"
            )

            print(
                f"    {tipo:6}"
                f"{linea.cuenta.nombre:25}"
                f"$ {linea.importe}"
            )

        # *************** LIBRO MAYOR
    print()

    print("----------------------------------------")
    print("LIBRO MAYOR")
    print("----------------------------------------")

    mayores = (
        ConsultarLibroMayor()
        .ejecutar(
            movimientos=movimientos,
        )
    )
    # for cuenta in mayores:
    #     print(
    #         cuenta.cuenta.nombre,
    #         len(cuenta.renglones),
    #     )
    # Recorrer las cuentas
    for cuenta in mayores:

        print()

        print(
            f"Cuenta: {cuenta.cuenta.nombre}"
        )

        print("-" * 40)
    # Recorrer los renglones
        for renglon in cuenta.renglones:

            tipo = (
                "Debe"
                if renglon.linea.es_debito()
                else "Haber"
            )

            print(
                f"{renglon.movimiento.fecha:%d/%m/%Y}  "
                f"{tipo:6}"
                f"{renglon.importe:>8}   "
                f"Saldo: {renglon.saldo}"
            )
        # Saldo final
        print()

        print(
            f"Saldo final: {cuenta.saldo}"
        )
    # La magia comienza. Quiero que me imprimas para estos 5 registros toda la info contable
    # Estado de Resultado
    print()

    print("----------------------------------------")
    print("ESTADO DE RESULTADOS")
    print("----------------------------------------")
    # Ahora usamos un servicio que ya existe en nuetro dominio
    estado_resultados = (
        ConsultarEstadoResultados()
        .ejecutar(
            movimientos=movimientos,
        )
    )
    for saldo in estado_resultados.saldos:

        print(
            f"{saldo.cuenta.nombre:25}"
            f"$ {saldo.saldo}"
        )   

    print()

    print(
        f"{'RESULTADO':25}"
        f"$ {estado_resultados.resultado}"
    )

    print()

    print("----------------------------------------")
    print("BALANCE DE SUMAS Y SALDOS")
    print("----------------------------------------")

    balance = (
        ConsultarBalanceSumasSaldos()
        .ejecutar(
            movimientos=movimientos,
        )
    )

    for fila in balance:

        saldo = fila.saldo

        if not fila.cuenta.naturaleza_deudora():
            saldo = -saldo

        print(
            f"{fila.cuenta.nombre:25}"
            f"Debe: {fila.total_debitos:>6}"
            f"   "
            f"Haber: {fila.total_creditos:>6}"
            f"   "
            f"Saldo: {saldo:>6}"
        )

        print()

    print("----------------------------------------")
    print("BALANCE GENERAL")
    print("----------------------------------------")

    balance = (
        ConsultarBalanceGeneral()
        .ejecutar(
            movimientos=movimientos,
        )
    )

    print()
    print("ACTIVOS")
    print("--------")

    for fila in balance.activos:

        print(
            f"{fila.cuenta.nombre:25}"
            f"$ {fila.saldo}"
        )

    print()

    print(
        f"{'TOTAL ACTIVOS':25}"
        f"$ {balance.total_activos}"
    )
    
    print()

    print("PASIVOS")
    print("--------")

    for fila in balance.pasivos:

        print(
            f"{fila.cuenta.nombre:25}"
            f"$ {fila.saldo}"
        )

    print()

    print(
        f"{'TOTAL PASIVOS':25}"
        f"$ {balance.total_pasivos}"
)
    print()

    print("PATRIMONIO")
    print("-----------")

    for fila in balance.patrimonio:

        print(
            f"{fila.cuenta.nombre:25}"
            f"$ {fila.saldo}"
        )

    print()

    print(
        f"{'TOTAL PATRIMONIO':25}"
        f"$ {balance.total_patrimonio}"
)

if __name__ == "__main__":
    main()