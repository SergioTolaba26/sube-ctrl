# Módulo Producto

## Objetivo

El módulo **Producto** centraliza toda la funcionalidad relacionada con los
productos comercializados por el sistema.

Este módulo será utilizado posteriormente por los módulos de:

- Compras
- Ventas
- Inventario
- Reportes

Su objetivo es ofrecer una única implementación para administrar productos,
evitando duplicación de código y manteniendo una arquitectura modular.

---

## Responsabilidades

Este módulo será responsable de:

- Crear productos.
- Modificar productos.
- Buscar productos.
- Listar productos.
- Eliminar productos (si la política del sistema lo permite).
- Validar datos del producto.
- Gestionar códigos de barras.

---

## No es responsabilidad de este módulo

Las siguientes funcionalidades pertenecen a otros módulos:

### Compras

- Registrar compras.
- Actualizar costos provenientes de una compra.

### Ventas

- Registrar ventas.
- Calcular importes de una venta.

### Inventario

- Actualizar stock.
- Movimientos de inventario.

### Contabilidad

- Generar asientos contables.

---

## Estructura del módulo

```
producto/

README.md

entity.py

repository.py

service.py

schemas.py

api.py

use_cases/

tests/
```

---

## Dependencias

El módulo Producto podrá ser utilizado por cualquier otro módulo.

Sin embargo, Producto no deberá depender de:

- Compras
- Ventas
- Inventario

De esta manera se evita el acoplamiento entre módulos.

---

## Filosofía de desarrollo

Cada modificación del módulo deberá cumplir el siguiente ciclo:

1. Objetivo.
2. Implementación.
3. Prueba.
4. Commit.

No deberán realizarse múltiples cambios funcionales en un mismo commit.

---

## Estado del módulo

Versión inicial.

Actualmente el módulo solo contiene documentación de arquitectura.

La implementación comenzará con la entidad `Producto`.