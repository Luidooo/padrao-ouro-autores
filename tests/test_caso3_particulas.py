import pytest

from caso3_particulas import Caso3Particulas


@pytest.mark.caso3
class TestCaso3Particulas:
    def setup_method(self):
        self.caso = Caso3Particulas()

    @pytest.mark.parametrize(
        "nome_a, nome_b",
        [
            ("Luiz de Oliveira de Souza", "Luiz Oliveira Souza"),
            ("Luiz de Oliveira de Souza", "Luiz de O. de Souza"),
            ("Maria de Souza Lima", "Maria Souza Lima"),
            ("Maria de Souza Lima", "Maria de S. Lima"),
        ],
    )
    def test_variantes_com_e_sem_particula_equivalem(self, nome_a, nome_b):
        assert self.caso.sao_equivalentes(nome_a, nome_b) is True

    @pytest.mark.parametrize(
        "nome_a, nome_b",
        [
            ("Luiz de Oliveira de Souza", "Maria de Souza Lima"),
            ("Luiz Oliveira Souza", "Pedro Oliveira Souza"),
        ],
    )
    def test_autores_diferentes_nao_equivalem(self, nome_a, nome_b):
        assert self.caso.sao_equivalentes(nome_a, nome_b) is False

    @pytest.mark.parametrize(
        "variantes, esperado",
        [
            (
                ["Luiz Oliveira Souza", "Luiz de Oliveira de Souza", "Luiz de O. de Souza"],
                "Luiz de Oliveira de Souza",
            ),
            (["Maria de S. Lima", "Maria de Souza Lima"], "Maria de Souza Lima"),
        ],
    )
    def test_unificar_escolhe_forma_completa_com_particula(self, variantes, esperado):
        assert self.caso.unificar(variantes) == esperado

    def test_unificar_lista_vazia_lanca_excecao(self):
        with pytest.raises(ValueError):
            self.caso.unificar([])
