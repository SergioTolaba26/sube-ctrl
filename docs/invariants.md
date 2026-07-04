Movimiento

- Debe representar un único hecho.

- Debe poseer al menos dos líneas.

Cuenta

- Debe tener un código.

- No almacena saldo.

LineaMovimiento

- Pertenece a un Movimiento.

- Afecta exactamente una Cuenta.

***********************************
# Invariantes del Dominio

## Objetivo

Este documento registra las reglas del negocio que siempre deben cumplirse.

Las invariantes forman parte del dominio y deben ser protegidas por las entidades.

---

## Cuenta

- Debe tener un código.
- Debe tener un nombre.
- No almacena el saldo.

---

## Movimiento

- Representa un único hecho del negocio.
- Debe mantener la consistencia de sus líneas.

---

## LíneaMovimiento

- Pertenece a un Movimiento.
- Afecta exactamente una Cuenta.