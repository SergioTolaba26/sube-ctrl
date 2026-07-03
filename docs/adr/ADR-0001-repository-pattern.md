# ADR-0001

## Título

El Movimiento constituye la unidad de registración del sistema.

---

## Estado

Aceptado

---

## Contexto

El proyecto comenzó como una aplicación para registrar gastos de transporte.

Durante el análisis del dominio se identificó que cualquier hecho económico (viaje, recarga, compra, venta, pago o transferencia) puede representarse mediante un modelo común.

---

## Decisión

Se adopta el Movimiento como unidad de registración.

Cada Movimiento estará compuesto por dos o más Líneas de Movimiento.

Cada Línea afectará exactamente una Cuenta.

Los saldos se obtendrán a partir de los movimientos registrados.

---

## Consecuencias

El modelo podrá evolucionar hacia:

- Finanzas Personales
- Inversiones
- Gestión Comercial
- Gestión Empresarial
- Contabilidad

sin modificar el núcleo del sistema.