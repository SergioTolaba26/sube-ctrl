1. Movimiento - Toda entidad debe existir porque el Negocio (no porque conviene para la Implementacion)
   | Sección | Contenido |
   | -------------------- | ---------------------------------------------------------------------------------------------------- |
   | Propósito | Registrar un hecho del negocio. |
   | Responsabilidades | Administrar sus líneas, garantizar la consistencia, representar un único hecho. |
   | No responsabilidades | Persistencia, HTTP, reportes. |
   | Relaciones | Contiene `LineaMovimiento`; puede asociarse a una `Categoría` y a un `Documento`. |
   | Invariantes | Debe cumplir las reglas del dominio (por ejemplo, cantidad mínima de líneas y consistencia interna). |

- Documentamos cómo debe comportarse la Entidad (Domain Driver Design)

---

# Entidades del Dominio

**Versión:** 1.0

**Estado:** Activo

---

# Objetivo

Este documento describe las entidades principales del dominio.

No define la implementación.

Define las responsabilidades del negocio.

Una entidad existe porque representa un concepto del dominio, no porque deba almacenarse en una base de datos.

---

# Empresa

## Propósito

Representar la organización propietaria de la información.

## Responsabilidades

- Mantener la identidad de la organización.
- Ser propietaria de cuentas, usuarios y movimientos.

## No responsabilidades

- Registrar movimientos.
- Calcular saldos.
- Gestionar persistencia.

## Relaciones

Posee:

- Usuarios
- Cuentas
- Movimientos

---

# Usuario

## Propósito

Representar una persona autorizada para operar el sistema.

## Responsabilidades

- Registrar operaciones.
- Consultar información.
- Ejecutar acciones permitidas.

## No responsabilidades

- Calcular saldos.
- Validar reglas contables.
- Persistir información.

## Relaciones

Pertenece a una Empresa.

---

# Cuenta

## Propósito

Representar un recurso económico.

## Responsabilidades

- Mantener su identidad.
- Recibir impactos mediante Líneas de Movimiento.
- Permitir obtener su saldo.

## No responsabilidades

- Registrar movimientos.
- Modificar otras cuentas.
- Persistir datos.

## Relaciones

Puede participar en muchas Líneas de Movimiento.

---

# Movimiento

## Propósito

Representar un hecho económico registrado por el sistema.

## Responsabilidades

- Mantener sus Líneas de Movimiento.
- Garantizar la consistencia del conjunto.
- Representar un único hecho del negocio.

## No responsabilidades

- Persistencia.
- HTTP.
- Reportes.
- Interfaz gráfica.

## Relaciones

Contiene dos o más Líneas de Movimiento.

Puede estar asociado a:

- Categoría
- Documento
- Usuario

## Invariantes

Debe poseer al menos dos Líneas.

Debe representar un único hecho del negocio.

No debe quedar en un estado inconsistente.

---

# Línea de Movimiento

## Propósito

Representar el efecto producido sobre una Cuenta.

## Responsabilidades

- Identificar la Cuenta afectada.
- Registrar el importe correspondiente.
- Formar parte de un Movimiento.

## No responsabilidades

- Existir independientemente.
- Crear movimientos.
- Calcular saldos globales.

## Relaciones

Pertenece a un único Movimiento.

Afecta exactamente una Cuenta.

## Invariantes

Debe pertenecer siempre a un Movimiento.

Debe afectar una única Cuenta.

---

# Principios

Las entidades deberán proteger sus propias reglas.

Los Services coordinan operaciones.

Los Repositories almacenan entidades.

La infraestructura nunca define el comportamiento del dominio.

---

Logica del negocio
Modelo rico
Movimiento

agregar_linea()

validar()

esta_balanceado()

eliminar_linea()

Luego el Servicio queda simple, algo como
MovimientoService

crear()

buscar()

guardar()
///////////////////////////
Entidades Ricas

Es decir:

Las entidades conocen las reglas del negocio.
Los Services orquestan casos de uso.
Los Repositories almacenan y recuperan entidades.
Los Routers solo exponen la API.

Cada capa tiene un propósito claro

Entidades son las guardianas de las reglas del negocio Ej Nueva regla - buscamos que Entidad debe protegerla