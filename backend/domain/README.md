# Domain

Este paquete contiene el modelo de dominio del sistema.

## Principios

- No depende de FastAPI.
- No depende de Storage.
- No depende de Repository.
- No depende de HTTP.
- No depende de JSON.
- No depende de PostgreSQL.

El dominio representa únicamente las reglas del negocio.

Toda dependencia debe apuntar hacia el dominio.

Nunca al revés.