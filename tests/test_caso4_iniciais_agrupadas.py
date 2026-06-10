import pytest

from caso4_iniciais_agrupadas import Caso4IniciaisAgrupadas


@pytest.mark.caso4
class TestCaso4IniciaisAgrupadas:
    def setup_method(self):
        self.caso = Caso4IniciaisAgrupadas()

    @pytest.mark.parametrize(
        "completo, agrupado",
        [
            ("Vanilda Cristina Junior", "VC Junior"),
            ("Sérgio Henrique Guaraldi", "SH Guaraldi"),
            ("Sergio Henrique Guaraldi", "SH Guaraldi"),
        ],
    )
    def test_iniciais_agrupadas_equivalem_ao_completo(self, completo, agrupado):
        assert self.caso.sao_equivalentes(completo, agrupado) is True

    @pytest.mark.parametrize(
        "nome_a, nome_b",
        [
            ("Vanilda Cristina Junior", "SH Guaraldi"),
            ("Vanilda Cristina Junior", "VC Souza"),
        ],
    )
    def test_autores_diferentes_nao_equivalem(self, nome_a, nome_b):
        assert self.caso.sao_equivalentes(nome_a, nome_b) is False

    @pytest.mark.parametrize(
        "variantes, esperado",
        [
            (["VC Junior", "Vanilda Cristina Junior"], "Vanilda Cristina Junior"),
            (["SH Guaraldi", "Sérgio Henrique Guaraldi"], "Sérgio Henrique Guaraldi"),
        ],
    )
    def test_unificar_escolhe_versao_completa(self, variantes, esperado):
        assert self.caso.unificar(variantes) == esperado

    def test_unificar_lista_vazia_lanca_excecao(self):
        with pytest.raises(ValueError):
            self.caso.unificar([])
