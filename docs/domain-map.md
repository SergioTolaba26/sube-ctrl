- Mapa conceptual del negocio
  Empresa
  │
  ┌────────┴────────┐
  │ │
  Usuarios Plan de Cuentas
  │
  Cuenta
  │
  Línea de Movimiento
  │
  Movimiento
  │
  Categoría Documento Tarifa

\*\* Nuestro trabajo es entender cómo funciona su negocio y representarlo de la manera más fiel posible.

Sprint 6 no implementaremos ninguna funcionalidad nueva que no haya sido previamente modelada y documentada.

Principios: El software no administra datos. Administra hechos del negocio
Modelo: 5 capas del Dominio
Realidad= ocurre fuera del sistema
│
▼
Evento del Negocio
│
▼
Movimiento
│
▼
Líneas de Movimiento
│
▼
Cuentas
│
▼
Evento del Negocio
│
▼
Movimiento
│
▼
Líneas de Movimiento
│
▼
Cuentas

---

ADN del sistema
Registro Universal

Todo hecho del negocio que produzca un efecto económico deberá representarse mediante un Movimiento compuesto por dos o más Líneas que afecten Cuentas.

¿Cuáles son los conceptos centrales?
¿Cuáles son las especializaciones?
¿Qué depende de qué?
¿Qué nunca debería depender de la infraestructura?
/////////////////////////////////////

# Domain Map

**Versión:** 1.0

**Estado:** En construcción

---

# Objetivo

Este documento describe el modelo conceptual del dominio.

No representa una implementación.

No depende de un lenguaje de programación.

No depende de una base de datos.

Su objetivo es representar el conocimiento del negocio.

---

# Filosofía

El sistema registra hechos del negocio.

Los hechos producen efectos económicos.

Los efectos económicos modifican recursos.

Todo ello queda registrado mediante movimientos.

---

# Núcleo del Dominio

El núcleo del sistema está formado por los siguientes conceptos.

Empresa

↓

Cuenta

↓

Movimiento

↓

LíneaMovimiento

Estos conceptos constituyen el corazón del sistema.

Su evolución deberá ser cuidadosamente analizada.

---

# Modelo Conceptual

Evento del negocio

↓

Movimiento

↓

LíneaMovimiento

↓

Cuenta

---

# Conceptos

## Empresa

Representa la organización propietaria de la información.

---

## Cuenta

Representa un recurso económico.

Ejemplos:

- Caja
- Banco
- Mercado Pago
- SUBE
- Cliente
- Proveedor
- Gastos
- Ingresos

---

## Movimiento

Representa un hecho del negocio registrado por el sistema.

Ejemplos:

- Viaje
- Compra
- Venta
- Pago
- Cobro
- Transferencia
- Recarga

Un Movimiento nunca modifica directamente el saldo.

Produce Líneas de Movimiento.

---

## LíneaMovimiento

Representa el efecto producido sobre una Cuenta.

Cada Línea afecta exactamente una Cuenta.

Todo Movimiento posee dos o más Líneas.

---

# Especializaciones

Las funcionalidades específicas se implementarán como especializaciones del núcleo.

Por ejemplo:

Transporte

↓

Viaje

↓

Movimiento

↓

LíneaMovimiento

↓

Cuenta

Otro ejemplo:

Inversiones

↓

Compra de Activo

↓

Movimiento

↓

LíneaMovimiento

↓

Cuenta

Otro ejemplo:

Medicamentos

↓

Compra

↓

Movimiento

↓

LíneaMovimiento

↓

Cuenta

---

# Reglas Fundamentales

1. Todo hecho económico deberá registrarse mediante un Movimiento.

2. Todo Movimiento deberá poseer al menos dos Líneas.

3. Toda Línea afectará exactamente una Cuenta.

4. Los saldos se obtendrán a partir de los Movimientos registrados.

5. El núcleo del dominio deberá permanecer estable.

---

# Evolución

El sistema podrá incorporar nuevos módulos sin modificar el núcleo.

Ejemplos futuros:

- Finanzas Personales

- Gestión Comercial

- Gestión Empresarial

- Contabilidad

- Inventario

- Recursos Humanos

Todos ellos deberán apoyarse sobre el mismo modelo conceptual.

---

# Principio Rector

No diseñamos funcionalidades.

Diseñamos un modelo capaz de representar la realidad del negocio.

La arquitectura técnica responde:

¿Cómo está construido?

La arquitectura del conocimiento responde:

¿Cómo entendemos el negocio?
***** Fin de cada documento con esta seccion *** Base: El conocimiento evoluciona.
Acá esta la escencia del proyecto
"El código implementa el sistema. El dominio explica por qué el sistema existe."
## Preguntas Abiertas

- ¿Debe existir la entidad Evento como concepto independiente?

- ¿Todo Movimiento debe estar asociado a un Documento?

- ¿Puede existir una Cuenta sin Movimientos?

- ¿Cómo representar ajustes o correcciones?

- ¿Cómo modelar anulaciones sin perder trazabilidad?

- ¿Cómo integrar la partida doble completa manteniendo la simplicidad para el usuario?

domain/base/value_object.py