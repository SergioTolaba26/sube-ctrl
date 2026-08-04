"""
Definición del esquema SQLite del ERP.

Cada sentencia CREATE TABLE debe agregarse a la lista SCHEMA.
"""

SCHEMA = [

    """
    CREATE TABLE IF NOT EXISTS productos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        codigo_barras TEXT NOT NULL UNIQUE,

        nombre TEXT NOT NULL,

        precio_compra REAL NOT NULL,

        activo INTEGER NOT NULL DEFAULT 1

    );
    """,

]