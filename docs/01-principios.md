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

\*\* COMO VAMOS A TRABAJAR

14. El núcleo del dominio debe cambiar lo menos posible.
    ¿Esta funcionalidad ya estaba prevista por el núcleo?" y no al reves "Necesitamos agregar una funcionalidad
    Los cambios en el nucleo (base el modelo conceptual) son poco frecuentes , los cambios en funcionalidades son frecuentes
    El nucle casi no se modifica en mas de 5 años si cambias las capacidades
    A medida que entendemos mejor la realidad que queremos representar, vamos descubriendo el nucleo que es la escencia de la ingenieria de software

Principio 18 – Crecimiento Orgánico del Dominio

Las entidades deben comenzar con el comportamiento mínimo necesario y evolucionar únicamente cuando el conocimiento del dominio lo justifique.

Principio 19 – Cada Sprint debe dejar el sistema un poco más comprensible, no solo un poco más grande.

/////// Pasamos de un Proyecto a una PLATAFORMA que puede ser la base de muchas aplicaciones
Principio 1

El dominio es el centro del sistema.

Principio 2

La infraestructura sirve al dominio, nunca al revés.

Principio 3

Toda regla del negocio vive dentro del dominio.

Principio 4

Las entidades evolucionan cuando el conocimiento evoluciona.

No antes.

Principio 5

Cada Sprint debe dejar el sistema mejor de lo que estaba.

No solamente con más funcionalidades.

Principio 6

La simplicidad inicial es una fortaleza, no una limitación.


Principio 20

Toda entidad existe para proteger la consistencia de su propio estado.

Principio 21

Cada Sprint entrega una versión estable, aunque todavía no sea la versión final.

Principio 22

Cada objeto es el experto en su propio estado y en las reglas que lo gobiernan.

Principio 23

Dentro del dominio preferimos relaciones entre objetos antes que referencias técnicas de persistencia.

Principio 24

La plataforma debe ser tan útil para crear software como para aprender a diseñarlo.
