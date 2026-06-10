from dataclasses import dataclass


@dataclass(frozen=True)
class Registro:
    id: int
    nome: str
