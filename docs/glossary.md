Término: Definición
Cuenta: Recurso económico cuyo valor puede variar a través de movimientos.
Movimiento: Representa un hecho registrado por el sistema que produce efectos económicos.
Línea de Movimiento: Impacto individual de un movimiento sobre una cuenta.
Categoría: Clasificación temática de un movimiento.
Tarifa: Valor de referencia utilizado para calcular determinados movimientos.

- Descubrir un lenguaje común para un motor de gestión

---

# Estado del documento

**Versión:** 1.0  
**Estado:** Activo  
**Última actualización:** 2026-07-02  
**Responsables:** Proyecto sube-ctrl

---

# Glosario del Dominio

## Introducción

Este documento define el lenguaje ubicuo del proyecto.

Cada término posee un único significado y deberá utilizarse de forma consistente en la documentación y en el código.

Cuando aparezca un nuevo concepto del negocio, deberá incorporarse primero a este glosario antes de ser implementado.

---

# Empresa

Organización propietaria de la información registrada por el sistema.

Inicialmente el sistema soportará una única empresa.

---

# Usuario

Persona autorizada para operar el sistema.

Puede registrar movimientos, consultar información y generar reportes.

---

# Cuenta

Representa un recurso económico cuyo valor puede variar a través del tiempo.

Ejemplos:

- Caja
- Banco
- Mercado Pago
- SUBE
- Cliente
- Proveedor
- Gasto Transporte
- Ingreso Sueldo

Una cuenta no almacena necesariamente su saldo.

El saldo puede obtenerse a partir de los movimientos registrados.

---

# Evento

Hecho ocurrido en el mundo real.

Ejemplos:

- Viaje
- Compra
- Venta
- Pago
- Cobro
- Transferencia
- Recarga

Un evento puede generar uno o más movimientos.

Inicialmente este concepto será únicamente parte del dominio y no tendrá implementación.

---

# Movimiento

Representa el registro de un hecho del negocio dentro del sistema.

Todo hecho económico deberá registrarse mediante un movimiento.

Un movimiento estará compuesto por dos o más líneas.

---

# Línea de Movimiento

Representa el impacto individual que un movimiento produce sobre una cuenta.

Cada línea afecta exactamente una cuenta.

Un movimiento contiene dos o más líneas.

---

# Categoría

Clasificación temática de un movimiento.

Ejemplos:

- Transporte
- Salud
- Alimentación
- Servicios
- Educación
- Inversiones

La categoría permite organizar y analizar la información.

No modifica saldos.

---

# Tarifa

Valor de referencia utilizado para calcular determinados movimientos.

Inicialmente se utilizará para transporte.

En el futuro podrán existir otros tipos de tarifas.

---

# Documento

Comprobante asociado a un movimiento.

Ejemplos:

- Ticket
- Factura
- Recibo
- Extracto

---

# Reporte

Información obtenida mediante el procesamiento de movimientos registrados.

Ejemplos:

- Gastos mensuales
- Saldo por cuenta
- Gastos por categoría
- Evolución del patrimonio

---

# Saldo

Resultado de acumular los efectos de los movimientos registrados sobre una cuenta.

El saldo no constituye un hecho del negocio.

Es una consecuencia de los movimientos.

---

# Principios del Lenguaje

- Un mismo término tendrá un único significado.
- El código utilizará los mismos nombres definidos en este documento.
- Antes de incorporar un nuevo concepto deberá evaluarse si ya existe uno equivalente.
- El dominio tiene prioridad sobre la tecnología.

\*\*Glosario -> evita usar una misma palabra y darle distinto significado. Importa que todos sepan que esta palabra para todos representa lo mismo
1 - Linea Movimiento (luego sera asiento pero sin conocimientos contables se entiende mejor lineMovimiento)
