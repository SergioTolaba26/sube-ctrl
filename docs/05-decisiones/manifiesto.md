Creemos que el software es la representación de un dominio, no solamente un conjunto de instrucciones.

Creemos que comprender el problema es más importante que programar la solución.

Creemos que documentar una decisión es tan importante como implementarla.

Creemos que la arquitectura debe facilitar la evolución, no impedirla.

Y creemos que la curiosidad es el motor que nos permite mejorar un poco cada día.

** ¿Qué aprendimos sobre el dominio que ayer no sabíamos?
** "La verdadera sabiduría está en reconocer los propios límites del conocimiento." Sócrates

---

Al principio, el proyecto era:

"Vamos a hacer una aplicación para controlar gastos de transporte."

Hoy, el proyecto es:

"Vamos a construir un motor de gestión con fundamentos sólidos, aprendiendo ingeniería de software en el proceso."

"¿Cuál es la mejor forma de representar la realidad?"

- Luego de cada Sprint
  ¿Qué construimos?
  ¿Qué aprendimos?
  ¿Qué nos gustaría explorar en el próximo Sprint?
  ++ ¿Como desarrollamos todo esto?
  "Pensamos primero. Modelamos después. Programamos al final."

Todo hecho del negocio se representa mediante un movimiento compuesto por líneas que afectan cuentas - Modelo sólido
Estamos para aprender a pensar Sistemas
Sprint 6 Dominio
Reglas

- Una Cuenta puede participar en muchos movimientos.
- Todo Movimiento debe contener al menos dos Líneas de Movimiento.
- Cada Línea afecta exactamente una Cuenta.
- Los movimientos nunca se modifican parcialmente.Si existe un error, debe corregirse mediante otro movimiento.=>historia y tanzabilidad.
- Toda operación debe poder reconstruirse a partir de los movimientos registrados.
