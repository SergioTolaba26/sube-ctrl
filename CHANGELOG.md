# Changelog
## v0.2.0

## Sprint 1
- Arquitectura base
- Configuración del proyecto

## Sprint 2
- Gestión de tarifas

## Sprint 3
- Gestión de saldo

# Changelog

## v0.2.0

### Agregado
- Jerarquía de cuentas.
- Navegación por ancestros.
- Navegación por descendientes.
- Ruta completa.
- Cuentas hoja.
- Validaciones de imputabilidad.
- Movimiento inmutable luego de confirmar.

*************************************
v0.10.0

- EmpresaRepositoryJson
- RegistrarEmpresa
- BuscarEmpresa
- ListarEmpresas
- 200 tests
*************************************
# Changelog

Todos los cambios importantes del proyecto se documentarán aquí.

## [0.12.0] - 2026-07-15

### Added
- BaseRepositoryJson para reutilizar la persistencia JSON.
- Tests de infraestructura para BaseRepositoryJson.

### Changed
- EmpresaRepositoryJson ahora hereda de BaseRepositoryJson.
- EjercicioRepositoryJson ahora hereda de BaseRepositoryJson.
- Eliminación de código duplicado en la capa de persistencia.

### Result
- 215 tests automatizados en verde.