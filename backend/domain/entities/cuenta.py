from __future__ import annotations

from pydantic import Field

from domain.base.entity import Entity
from domain.enums.tipo_cuenta import TipoCuenta

from decimal import Decimal
from domain.enums.tipo_afectacion import TipoAfectacion


class Cuenta(Entity):
    """
    Representa un recurso económico del negocio.

    Una Cuenta no almacena su saldo.
    El saldo se obtiene a partir de las Líneas de Movimiento.
    """

    codigo: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Código único de la cuenta."
    )

    nombre: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Nombre descriptivo de la cuenta."
    )

    tipo: TipoCuenta = Field(
        ...,
        description="Tipo de cuenta."
    )

    activa: bool = Field(
        default=True,
        description="Indica si la cuenta puede utilizarse."
    )
    imputable: bool = Field(
    default=True,
    description="Indica si la cuenta admite movimientos."
    )

    padre: Cuenta | None = Field(
    default=None,
    description="Cuenta padre dentro del plan de cuentas."
    )
    hijos: list[Cuenta] = Field(
    default_factory=list,
    description="Cuentas hijas."
    )
    def activar(self) -> None:
        """Activa la cuenta."""
        self.activa = True

    def desactivar(self) -> None:
        """Desactiva la cuenta."""
        self.activa = False

    def hacer_no_imputable(self) -> None:
        """
        Impide que la cuenta reciba movimientos.
        """
        self.imputable = False

    def hacer_imputable(self) -> None:
        """
        Permite nuevamente registrar movimientos en la cuenta.
        """
        self.imputable = True

    def es_imputable(self) -> bool:
        """
        Indica si la cuenta admite recibir movimientos.
        """
        return self.imputable
    

    def esta_activa(self) -> bool:
        """Indica si la cuenta está activa."""
        return self.activa
    
    def naturaleza_deudora(self) -> bool:
        """
        Indica si la cuenta posee naturaleza deudora.
        """

        return self.tipo.es_naturaleza_deudora()

    def renombrar(self, nuevo_nombre: str) -> None:
        """
        Cambia el nombre de la cuenta.
        """

        nuevo_nombre = nuevo_nombre.strip()

        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacío.")

        self.nombre = nuevo_nombre

    def asignar_padre(self, padre: Cuenta) -> None:
        """
        Asigna una cuenta padre.
        """

        if padre is self:
            raise ValueError(
                "Una cuenta no puede ser padre de sí misma."
            )

        if self in padre.ancestros():
            raise ValueError(
                "No se puede generar un ciclo en el árbol."
            )

        if self.padre is not None:
            raise ValueError(
                "La cuenta ya tiene una cuenta padre."
            )

        padre.hacer_no_imputable()

        self.padre = padre
        padre.hijos.append(self)

    def ancestros(self) -> list[Cuenta]:
        """
        Devuelve la lista de ancestros de la cuenta,
        comenzando por el padre inmediato hasta la raíz.
        """

        ancestros: list[Cuenta] = []

        actual = self.padre

        while actual is not None:
            ancestros.append(actual)
            actual = actual.padre

        return ancestros

    def descendientes(self) -> list[Cuenta]:
        """
        Devuelve todos los descendientes de la cuenta
        recorriendo el árbol en profundidad.
        """

        resultado: list[Cuenta] = []

        for hijo in self.hijos:
            resultado.append(hijo)
            resultado.extend(hijo.descendientes())

        return resultado
    
    def es_hoja(self) -> bool:
        """
        Indica si la cuenta no posee cuentas hijas.
        """

        return not self.hijos
    
    def nivel(self) -> int:
        """
        Devuelve el nivel que ocupa la cuenta
        dentro del árbol del plan de cuentas.
        """

        return len(self.ancestros())
    
    def ruta(self) -> list[Cuenta]:
        """
        Devuelve la ruta desde la cuenta raíz
        hasta esta cuenta.
        """

        ruta = list(reversed(self.ancestros()))
        ruta.append(self)

        return ruta

    def aplicar_afectacion(
        self,
        saldo_actual: Decimal,
        tipo_afectacion: TipoAfectacion,
        importe: Decimal,
    ) -> Decimal:
        """
        Devuelve el nuevo saldo luego de aplicar
        una afectación sobre esta cuenta.
        """

        if self.naturaleza_deudora():

            if tipo_afectacion == TipoAfectacion.DEBITO:
                return saldo_actual + importe

            return saldo_actual - importe

        if tipo_afectacion == TipoAfectacion.CREDITO:
            return saldo_actual + importe

        return saldo_actual - importe
    


    def calcular_saldo(
        self,
        total_debitos: Decimal,
        total_creditos: Decimal,
    ) -> Decimal:
        """
        Calcula el saldo de la cuenta a partir de los
        totales de débitos y créditos.
        """

        if self.naturaleza_deudora():
            return total_debitos - total_creditos

        return total_creditos - total_debitos