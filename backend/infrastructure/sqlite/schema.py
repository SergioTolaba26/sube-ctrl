"""
Definición del esquema SQLite del ERP.

Cada sentencia CREATE TABLE debe agregarse a la lista SCHEMA.
"""

SCHEMA = [

    """
    CREATE TABLE IF NOT EXISTS productos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        empresa_id INTEGER NOT NULL,

        codigo_barras TEXT NOT NULL,

        nombre TEXT NOT NULL,

        precio_compra REAL NOT NULL,

        activo INTEGER NOT NULL DEFAULT 1,

        UNIQUE (empresa_id, codigo_barras)

    );
    """,

]