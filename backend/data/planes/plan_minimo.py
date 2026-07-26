from domain.enums.tipo_cuenta import TipoCuenta

PLAN_MINIMO = [

    # ACTIVO

    {
        "codigo": "1.1.01",
        "nombre": "Caja",
        "tipo": TipoCuenta.ACTIVO,
        "imputable": True,
    },

    {
        "codigo": "1.1.02",
        "nombre": "Banco",
        "tipo": TipoCuenta.ACTIVO,
        "imputable": True,
    },

    {
        "codigo": "1.2.01",
        "nombre": "Clientes",
        "tipo": TipoCuenta.ACTIVO,
        "imputable": True,
    },

    # PASIVO

    {
        "codigo": "2.1.01",
        "nombre": "Proveedores",
        "tipo": TipoCuenta.PASIVO,
        "imputable": True,
    },

    {
        "codigo": "2.2.01",
        "nombre": "Préstamos",
        "tipo": TipoCuenta.PASIVO,
        "imputable": True,
    },

    # PATRIMONIO

    {
        "codigo": "3.1.01",
        "nombre": "Capital",
        "tipo": TipoCuenta.PATRIMONIO,
        "imputable": True,
    },

    # INGRESOS

    {
        "codigo": "4.1.01",
        "nombre": "Ventas",
        "tipo": TipoCuenta.INGRESO,
        "imputable": True,
    },

    # GASTOS

    {
        "codigo": "5.1.01",
        "nombre": "Compras",
        "tipo": TipoCuenta.GASTO,
        "imputable": True,
    },

    {
        "codigo": "5.2.01",
        "nombre": "Sueldos",
        "tipo": TipoCuenta.GASTO,
        "imputable": True,
    },

    {
        "codigo": "5.3.01",
        "nombre": "Servicios",
        "tipo": TipoCuenta.GASTO,
        "imputable": True,
    },
]