from normalizacao import colapsar_espacos, remover_acentos

_PARTICULAS = {"de", "da", "do", "dos", "das", "e"}


class Caso4IniciaisAgrupadas:
    def _normalizar(self, token: str) -> str:
        return remover_acentos(token).lower().replace(".", "")

    def _eh_grupo_iniciais(self, token: str) -> bool:
        return token.isalpha() and token.isupper() and len(token) >= 2

    def _eh_inicial(self, token: str) -> bool:
        return len(token.replace(".", "")) == 1

    def _significativos(self, nome: str) -> list[str]:
        tokens = colapsar_espacos(nome).split()
        return [t for t in tokens if self._normalizar(t) not in _PARTICULAS]

    def _assinatura(self, nome: str) -> tuple[str, tuple[str, ...]]:
        significativos = self._significativos(nome)
        sobrenome = significativos[-1]
        iniciais: list[str] = []
        for token in significativos[:-1]:
            if self._eh_grupo_iniciais(token):
                iniciais.extend(self._normalizar(token))
            else:
                iniciais.append(self._normalizar(token)[0])
        return self._normalizar(sobrenome), tuple(iniciais)

    def sao_equivalentes(self, nome_a: str, nome_b: str) -> bool:
        return self._assinatura(nome_a) == self._assinatura(nome_b)

    def _qtd_por_extenso(self, nome: str) -> int:
        return sum(
            1
            for t in self._significativos(nome)
            if not self._eh_grupo_iniciais(t) and not self._eh_inicial(t)
        )

    def unificar(self, nomes: list[str]) -> str:
        if not nomes:
            raise ValueError("a lista de nomes nao pode ser vazia")
        return max(nomes, key=lambda n: (self._qtd_por_extenso(n), len(n)))
