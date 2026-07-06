from normalizacao import colapsar_espacos, remover_acentos

_PARTICULAS = {"de", "da", "do", "dos", "das", "e"}

# ---> CLASSE OBJETO-MÉTODO EXTRAÍDA AQUI <---
class AvaliadorEquivalencia:
    def __init__(self, caso_instancia, nome_a: str, nome_b: str):
        self.caso = caso_instancia
        self.nome_a = nome_a
        self.nome_b = nome_b

    def computar(self) -> bool:
        sig_a = self.caso._significativos(self.nome_a)
        sig_b = self.caso._significativos(self.nome_b)
        if len(sig_a) != len(sig_b):
            return False
        return all(self.caso._tokens_combinam(a, b) for a, b in zip(sig_a, sig_b))
# --------------------------------------------


class Caso3Particulas:
    def _normalizar(self, token: str) -> str:
        return remover_acentos(token).lower().replace(".", "")

    def _eh_inicial(self, token: str) -> bool:
        return len(token.replace(".", "")) == 1

    def _significativos(self, nome: str) -> list[str]:
        tokens = colapsar_espacos(nome).split()
        return [t for t in tokens if self._normalizar(t) not in _PARTICULAS]

    def _tokens_combinam(self, a: str, b: str) -> bool:
        na, nb = self._normalizar(a), self._normalizar(b)
        if self._eh_inicial(a) or self._eh_inicial(b):
            return na[0] == nb[0]
        return na == nb

    def sao_equivalentes(self, nome_a: str, nome_b: str) -> bool:
        # Uso do Objeto-Método
        avaliador = AvaliadorEquivalencia(self, nome_a, nome_b)
        return avaliador.computar()

    def _qtd_por_extenso(self, nome: str) -> int:
        return sum(1 for t in self._significativos(nome) if not self._eh_inicial(t))

    def unificar(self, nomes: list[str]) -> str:
        if not nomes:
            raise ValueError("a lista de nomes nao pode ser vazia")
        return max(
            nomes,
            key=lambda n: (self._qtd_por_extenso(n), len(colapsar_espacos(n).split()), len(n)),
        )