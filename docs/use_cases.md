# Casos de Uso = MUESTRA COMO INTERACTUAN LAS ENTIDADES, describen cómo colaboran - Caso de uso no pertenece al Dominio

Caso de uso sabe como registrar un viaje

- Entidades describen qué son, pertenece al Dominio y el Dominio sabe qué es un Movimiento

## Registrar un viaje

Actor:
Usuario

Objetivo:
Registrar un viaje realizado utilizando la tarjeta SUBE.

Flujo:

1. Se identifica la tarifa.
2. Se crea un Movimiento.
3. Se agregan las Líneas correspondientes.
4. Se valida el Movimiento.
5. Se guarda el Movimiento.

Resultado:

El hecho económico queda registrado.
