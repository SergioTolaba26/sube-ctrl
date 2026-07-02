# Principios del Proyecto

## Introducción

Este documento define los principios que guían el diseño, desarrollo y evolución del proyecto.

Estos principios tienen prioridad sobre decisiones puntuales de implementación y servirán como referencia para mantener una arquitectura consistente en el tiempo.

---

# 1. El dominio primero

Antes de escribir código debemos comprender el problema que queremos resolver.

Las entidades, relaciones y reglas del negocio son más importantes que la tecnología utilizada.

El dominio nunca debe depender del framework.

---

# 2. Simplicidad

Siempre elegiremos la solución más simple que resuelva correctamente el problema.

No agregaremos complejidad anticipando necesidades futuras que todavía no existen.

La escalabilidad debe lograrse mediante un buen diseño, no mediante una arquitectura innecesariamente compleja.

---

# 3. Arquitectura por capas

Cada capa tiene una única responsabilidad.

Frontend
↓
Router
↓
Service
↓
Repository
↓
Storage

Las capas superiores desconocen los detalles internos de las inferiores.

---

# 4. Separación de responsabilidades

Cada clase debe tener un único motivo para cambiar.

Una clase pequeña y clara es preferible a una clase grande con múltiples responsabilidades.

---

# 5. Reutilización

Antes de duplicar código, analizaremos si puede abstraerse en un componente reutilizable.

La reutilización debe mejorar la claridad del proyecto y no complicarlo.

---

# 6. Documentación viva

La documentación forma parte del proyecto.

Cada decisión importante debe quedar registrada.

La documentación evolucionará junto con el código.

---

# 7. Calidad antes que velocidad

Preferimos avanzar más lentamente si eso garantiza una mejor arquitectura y una mayor mantenibilidad.

No se aceptarán atajos que generen deuda técnica innecesaria.

---

# 8. Escalabilidad

Cada decisión deberá considerar la evolución futura del proyecto.

El objetivo es permitir que nuevos módulos reutilicen el núcleo existente.

---

# 9. Independencia tecnológica

El modelo de dominio no debe depender de:

- FastAPI
- JSON
- SQLite
- PostgreSQL
- React
- PWA

La tecnología puede cambiar.

El dominio debe permanecer estable.

---

# 10. Aprendizaje continuo

Este proyecto tiene un doble propósito:

- construir una aplicación útil;
- desarrollar conocimientos sólidos de arquitectura de software.

Cada Sprint deberá aportar nuevas funcionalidades y nuevos aprendizajes.

---

# Nuestra filosofía

Lento.

Ordenado.

Documentado.

Preparado para crecer.

** COMO VAMOS A TRABAJAR