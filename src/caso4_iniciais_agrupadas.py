from normalizacao import colapsar_espacos, remover_acentos

_PARTICULAS = {"de", "da", "do", "dos", "das", "e"}


# ---> NOVA CLASSE EXTRAÍDA <---
class AnalisadorTokens:
    def normalizar(self, token: str) -> str:
        return remover_acentos(token).lower().replace(".", "")

    def eh_grupo_iniciais(self, token: str) -> bool:
        return token.isalpha() and token.isupper() and len(token) >= 2

    def eh_inicial(self, token: str) -> bool:
        return len(token.replace(".", "")) == 1

    def significativos(self, nome: str) -> list[str]:
        tokens = colapsar_espacos(nome).split()
        return [t for t in tokens if self.normalizar(t) not in _PARTICULAS]
# ------------------------------


class Caso4IniciaisAgrupadas:
    def __init__(self):
        # A classe original agora delega a análise de texto para a nova classe
        self.analisador = AnalisadorTokens()

    def _assinatura(self, nome: str) -> tuple[str, tuple[str, ...]]:
        significativos = self.analisador.significativos(nome)
        sobrenome = significativos[-1]
        iniciais: list[str] = []
        for token in significativos[:-1]:
            if self.analisador.eh_grupo_iniciais(token):
                iniciais.extend(self.analisador.normalizar(token))
            else:
                iniciais.append(self.analisador.normalizar(token)[0])
        return self.analisador.normalizar(sobrenome), tuple(iniciais)

    def sao_equivalentes(self, nome_a: str, nome_b: str) -> bool:
        return self._assinatura(nome_a) == self._assinatura(nome_b)

    def _qtd_por_extenso(self, nome: str) -> int:
        return sum(
            1
            for t in self.analisador.significativos(nome)
            if not self.analisador.eh_grupo_iniciais(t) and not self.analisador.eh_inicial(t)
        )

    def unificar(self, nomes: list[str]) -> str:
        if not nomes:
            raise ValueError("a lista de nomes nao pode ser vazia")
        return max(nomes, key=lambda n: (self._qtd_por_extenso(n), len(n)))