from normalizacao import colapsar_espacos, remover_acentos

_PARTICULAS = {"de", "da", "do", "dos", "das", "e"}


class Caso2SobrenomeIniciais:
    def _normalizar(self, token: str) -> str:
        return remover_acentos(token).lower().replace(".", "")

    def _eh_inicial(self, token: str) -> bool:
        return len(token.replace(".", "")) == 1

    def _significativos(self, nome: str) -> list[str]:
        tokens = colapsar_espacos(nome).split()
        return [t for t in tokens if self._normalizar(t) not in _PARTICULAS]

    # ---> MÉTODO EXTRAÍDO AQUI <---
    def _separar_nome_sobrenome(self, significativos: list[str]) -> tuple[str, list[str]]:
        iniciais = [t for t in significativos if self._eh_inicial(t)]
        por_extenso = [t for t in significativos if not self._eh_inicial(t)]

        if iniciais and len(por_extenso) == 1:
            sobrenome = por_extenso[0]
            nomes = iniciais
        else:
            sobrenome = significativos[-1]
            nomes = significativos[:-1]
            
        return sobrenome, nomes
    # ------------------------------

    def _assinatura(self, nome: str) -> tuple[str, tuple[str, ...]]:
        significativos = self._significativos(nome)
        
        # Uso do método extraído
        sobrenome, nomes = self._separar_nome_sobrenome(significativos)

        return self._normalizar(sobrenome), tuple(self._normalizar(n)[0] for n in nomes)

    def sao_equivalentes(self, nome_a: str, nome_b: str) -> bool:
        return self._assinatura(nome_a) == self._assinatura(nome_b)

    def _qtd_por_extenso(self, nome: str) -> int:
        return sum(1 for t in self._significativos(nome) if not self._eh_inicial(t))

    def unificar(self, nomes: list[str]) -> str:
        if not nomes:
            raise ValueError("a lista de nomes nao pode ser vazia")
        return max(nomes, key=lambda n: (self._qtd_por_extenso(n), len(n)))