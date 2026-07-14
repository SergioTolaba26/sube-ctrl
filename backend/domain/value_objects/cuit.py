from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Cuit:

    valor: str

    def __post_init__(self):

        limpio = self.valor.replace("-", "")

        if len(limpio) != 11:
            raise ValueError(
                "El CUIT debe contener 11 dígitos."
            )

        object.__setattr__(
            self,
            "valor",
            f"{limpio[:2]}-{limpio[2:10]}-{limpio[10]}"
        )