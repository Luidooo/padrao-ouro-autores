import pytest

from caso2_sobrenome_iniciais import Caso2SobrenomeIniciais


@pytest.mark.caso2
class TestCaso2SobrenomeIniciais:
    def setup_method(self):
        self.caso = Caso2SobrenomeIniciais()

    @pytest.mark.parametrize(
        "completo, abreviado",
        [
            ("Ana de Mattos Seabra", "Seabra A M"),
            ("Ana de Mattos Seabra", "Seabra A. M."),
            ("Cassius de Souza", "Souza C."),
            ("Cassius de Souza", "Souza C"),
        ],
    )
    def test_abreviado_equivale_ao_completo(self, completo, abreviado):
        assert self.caso.sao_equivalentes(completo, abreviado) is True

    @pytest.mark.parametrize(
        "nome_a, nome_b",
        [
            ("Ana de Mattos Seabra", "Souza C."),
            ("Cassius de Souza", "Seabra A M"),
        ],
    )
    def test_autores_diferentes_nao_equivalem(self, nome_a, nome_b):
        assert self.caso.sao_equivalentes(nome_a, nome_b) is False

    @pytest.mark.parametrize(
        "variantes, esperado",
        [
            (["Ana de Mattos Seabra", "Seabra A M"], "Ana de Mattos Seabra"),
            (["Souza C.", "Cassius de Souza"], "Cassius de Souza"),
        ],
    )
    def test_unificar_escolhe_versao_completa(self, variantes, esperado):
        assert self.caso.unificar(variantes) == esperado

    def test_unificar_lista_vazia_lanca_excecao(self):
        with pytest.raises(ValueError):
            self.caso.unificar([])
