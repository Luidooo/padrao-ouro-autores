from normalizacao import (
    colapsar_espacos,
    contar_acentos,
    normalizar_apostrofo,
    remover_acentos,
)


class Caso1Tipografico:
    def chave(self, nome: str) -> str:
        sem_apostrofo = normalizar_apostrofo(nome)
        sem_acento = remover_acentos(sem_apostrofo)
        return colapsar_espacos(sem_acento.lower())

    def sao_equivalentes(self, nome_a: str, nome_b: str) -> bool:
        return self.chave(nome_a) == self.chave(nome_b)

    def unificar(self, nomes: list[str]) -> str:
        if not nomes:
            raise ValueError("a lista de nomes nao pode ser vazia")
        mais_acentuado = max(nomes, key=lambda n: (contar_acentos(n), len(n)))
        return normalizar_apostrofo(mais_acentuado)
