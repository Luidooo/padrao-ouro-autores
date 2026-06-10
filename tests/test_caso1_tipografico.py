"""Testes do Caso 1 - diferencas tipograficas (acentos / cedilha / apostrofo).

A unidade unifica variantes que diferem apenas na grafia para a forma
padrao-ouro: corretamente acentuada e com apostrofo reto (').
"""
import pytest

from caso1_tipografico import Caso1Tipografico


@pytest.mark.caso1
class TestCaso1Tipografico:
    """Suite de testes do Caso 1."""

    def setup_method(self):
        self.caso = Caso1Tipografico()

    # --- equivalencia: variantes do mesmo autor ---
    @pytest.mark.parametrize(
        "nome_a, nome_b",
        [
            ("Monica Hirata Sant`anna", "Mônica Hirata Sant'anna"),
            ("Sergio Henrique Guaraldi", "Sérgio Henrique Guaraldi"),
            ("Veronica de Oliveira Moreira", "Verônica de Oliveira Moreira"),
        ],
    )
    def test_variantes_tipograficas_sao_equivalentes(self, nome_a, nome_b):
        assert self.caso.sao_equivalentes(nome_a, nome_b) is True

    # --- nao-equivalencia: autores diferentes ---
    @pytest.mark.parametrize(
        "nome_a, nome_b",
        [
            ("Sérgio Henrique Guaraldi", "Raphael Goncalves Viana"),
            ("Mônica Hirata Sant'anna", "Ana de Mattos Seabra"),
        ],
    )
    def test_autores_diferentes_nao_sao_equivalentes(self, nome_a, nome_b):
        assert self.caso.sao_equivalentes(nome_a, nome_b) is False

    # --- unificacao para a forma padrao-ouro ---
    @pytest.mark.parametrize(
        "variantes, esperado",
        [
            (
                ["Monica Hirata Sant`anna", "Mônica Hirata Sant'anna"],
                "Mônica Hirata Sant'anna",
            ),
            (
                ["Sergio Henrique Guaraldi", "Sérgio Henrique Guaraldi"],
                "Sérgio Henrique Guaraldi",
            ),
            (
                ["Veronica de Oliveira Moreira", "Verônica de Oliveira Moreira"],
                "Verônica de Oliveira Moreira",
            ),
        ],
    )
    def test_unificar_escolhe_forma_acentuada_correta(self, variantes, esperado):
        assert self.caso.unificar(variantes) == esperado

    # --- teste de excecao ---
    def test_unificar_lista_vazia_lanca_excecao(self):
        with pytest.raises(ValueError):
            self.caso.unificar([])
