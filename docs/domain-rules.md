# Domain Rules

## Objetivo

Este documento define las reglas del dominio.

Las reglas representan restricciones del negocio.

Las entidades son responsables de protegerlas.

---

# Cuenta

## DR-001

Toda Cuenta debe tener un código único.

Estado: Pendiente de implementación.

---

## DR-002

Toda Cuenta debe poseer un nombre.

Estado: Implementado.

---

## DR-003

Una Cuenta inactiva no puede recibir nuevos Movimientos.

Estado: Pendiente.

---

# Movimiento

## DR-101

Todo Movimiento representa un único hecho del negocio.

Estado: Implementado conceptualmente.

---

## DR-102

Todo Movimiento debe contener al menos dos Líneas.

Estado: Pendiente.

---

## DR-103

Las Líneas pertenecen exclusivamente a un Movimiento.

Estado: Pendiente.

---

# LíneaMovimiento

## DR-201

Toda Línea debe afectar exactamente una Cuenta.

Estado: Pendiente.

---

## DR-202

Una Línea no puede existir sin un Movimiento.

Estado: Pendiente.

---

# Principio

Las reglas del negocio pertenecen al dominio.

Nunca a la infraestructura.