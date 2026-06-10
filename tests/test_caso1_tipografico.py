import pytest

from caso1_tipografico import Caso1Tipografico


@pytest.mark.caso1
class TestCaso1Tipografico:
    def setup_method(self):
        self.caso = Caso1Tipografico()

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

    @pytest.mark.parametrize(
        "nome_a, nome_b",
        [
            ("Sérgio Henrique Guaraldi", "Raphael Goncalves Viana"),
            ("Mônica Hirata Sant'anna", "Ana de Mattos Seabra"),
        ],
    )
    def test_autores_diferentes_nao_sao_equivalentes(self, nome_a, nome_b):
        assert self.caso.sao_equivalentes(nome_a, nome_b) is False

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

    def test_unificar_lista_vazia_lanca_excecao(self):
        with pytest.raises(ValueError):
            self.caso.unificar([])
