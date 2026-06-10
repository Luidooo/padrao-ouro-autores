from registro import Registro


class Caso5Identificadores:
    def id_canonico(self, ids: list[int]) -> int:
        if not ids:
            raise ValueError("a lista de ids nao pode ser vazia")
        return min(ids)

    def unificar(self, registros: list[Registro]) -> list[Registro]:
        if not registros:
            raise ValueError("a lista de registros nao pode ser vazia")
        menor = self.id_canonico([r.id for r in registros])
        return [Registro(menor, r.nome) for r in registros]
