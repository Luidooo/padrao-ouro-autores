import pytest

from caso5_identificadores import Caso5Identificadores
from registro import Registro


@pytest.mark.caso5
class TestCaso5Identificadores:
    def setup_method(self):
        self.caso = Caso5Identificadores()

    @pytest.mark.parametrize(
        "ids, esperado",
        [
            ([31298, 433094, 549243, 608297, 746938], 31298),
            ([554799, 243350, 954057], 243350),
        ],
    )
    def test_id_canonico_e_o_menor(self, ids, esperado):
        assert self.caso.id_canonico(ids) == esperado

    @pytest.mark.parametrize(
        "registros, menor",
        [
            (
                [
                    Registro(31298, "Raphael Goncalves Viana"),
                    Registro(433094, "Raphael Gonçalves Viana"),
                    Registro(746938, "Raphael Gonçalves Viana"),
                ],
                31298,
            ),
            (
                [
                    Registro(954057, "Sérgio Henrique Guaraldi"),
                    Registro(243350, "Sérgio Henrique Guaraldi"),
                ],
                243350,
            ),
        ],
    )
    def test_unificar_mapeia_todos_para_o_menor_id(self, registros, menor):
        resultado = self.caso.unificar(registros)
        assert all(r.id == menor for r in resultado)
        assert [r.nome for r in resultado] == [r.nome for r in registros]

    def test_id_canonico_lista_vazia_lanca_excecao(self):
        with pytest.raises(ValueError):
            self.caso.id_canonico([])

    def test_unificar_lista_vazia_lanca_excecao(self):
        with pytest.raises(ValueError):
            self.caso.unificar([])
