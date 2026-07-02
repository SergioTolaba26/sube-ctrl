\*\* QUE COSAS EXISTEN EN NUETRO MUNDO

# Estado del documento

**Versión:** 1.0
**Estado:** En evolución
**Última actualización:** 2026-07-02
**Responsables:** Proyecto sube-ctrl

---

# Dominio del Proyecto

## Introducción

Este documento define el modelo conceptual del sistema.

No describe la implementación técnica.

Describe los conceptos del negocio y las relaciones entre ellos.

Las clases del proyecto deberán reflejar este dominio.

---

# Filosofía del Dominio

Todo sistema de gestión puede entenderse como un conjunto de eventos que modifican el estado de determinados recursos.

Nuestro objetivo consiste en representar esos eventos de forma simple, consistente y reutilizable.

---

# Conceptos Fundamentales

## Empresa

Representa la organización propietaria de la información.

Inicialmente el sistema funcionará para una única empresa.

En el futuro podrá soportar múltiples empresas.

---

## Usuario

Representa una persona autorizada a operar el sistema.

Los usuarios podrán registrar movimientos y consultar información.

---

## Cuenta

Representa cualquier recurso cuyo saldo pueda modificarse.

Ejemplos:

- SUBE
- Caja
- Banco
- Mercado Pago
- Tarjeta de Crédito
- Cliente
- Proveedor

Toda modificación económica ocurre sobre una o más cuentas.

---

## Movimiento

Representa un hecho económico que modifica el saldo de una o más cuentas.

Ejemplos:

- Recarga SUBE
- Viaje
- Compra
- Venta
- Pago
- Cobro
- Transferencia
- Ajuste

El movimiento constituye la unidad principal de registración del sistema.

---

## Categoría

Permite clasificar movimientos según su naturaleza.

Ejemplos:

- Transporte
- Alimentación
- Salud
- Inversiones
- Impuestos

---

## Tarifa

Representa un valor de referencia utilizado para calcular determinados movimientos.

Inicialmente se utilizará para transporte.

En otros módulos podrán existir diferentes tipos de tarifas.

---

## Reporte

Representa información obtenida a partir del procesamiento de movimientos.

Ejemplos:

- Gastos mensuales
- Gastos por categoría
- Saldo por cuenta
- Historial de movimientos

---

# Conceptos futuros

Estos conceptos todavía no forman parte de la implementación, pero el dominio se diseña considerando su futura incorporación.

## Plan de Cuentas

Agrupa y organiza las cuentas del sistema.

---

## Asiento Contable

Representa la registración contable de un movimiento bajo el principio de partida doble.

Inicialmente no será obligatorio.

En futuras versiones podrá generarse automáticamente.

---

## Centro de Costo

Permite clasificar movimientos según sectores, proyectos o unidades de negocio.

---

## Documento

Representa el comprobante asociado a un movimiento.

Ejemplos:

- Factura
- Ticket
- Recibo

---

# Relaciones principales

Empresa
│
└── Usuarios

Empresa
│
└── Cuentas

Cuenta
│
└── Movimientos

Movimiento
│
├── Categoría
│
└── Tarifa (opcional)

Movimiento
│
└── Reportes

En futuras versiones:

Movimiento
│
└── Asiento Contable

///////////////////////////////////////////////
Version 1.1
ERP modernos: la separación entre Entidad, Evento y Movimiento.
Entidad
│
├── Empresa
├── Usuario
├── Cuenta
├── Tarifa
└── Categoría

Evento
│
├── Viaje
├── Recarga
├── Compra
├── Venta
├── Pago
└── Cobro

Movimiento
│
└── Impacto económico generado por un evento
 
 **********************
 Metodologia

 Pensar
    ↓
Documentar
    ↓
Modelar
    ↓
Programar
    ↓
Probar
    ↓
Documentar lo aprendido

// Nueva Seccion
## Principio de Registración

El Movimiento constituye la única fuente de verdad del sistema.

Toda modificación económica deberá registrarse como uno o más movimientos.

Los saldos, reportes y estadísticas deberán obtenerse a partir de dichos movimientos.

En el futuro podrán existir mecanismos de optimización (caché o resúmenes), pero nunca reemplazarán la registración original.