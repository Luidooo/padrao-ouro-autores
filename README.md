# padrao-ouro-autores

Trabalho Prático 1 (TDD) — **TPPE / FGA0242 — Técnicas de Programação para Plataformas Emergentes**
Universidade de Brasília — FCTE.

Curadoria e **deduplicação de nomes de autores** em registros de informação
científica. O sistema unifica diferentes grafias/representações de um mesmo
autor para uma representação canônica (padrão-ouro), cobrindo os 5 casos
descritos no enunciado.

## Integrantes do grupo

| Nome | Matrícula |
|------|-----------|
| Luis Eduardo Castro Mendes de Lima | 221008285 |
| Henrique Carvalho Neves | 222006801 |
| Caio Falcão Habibe Costa | 221021868 |

## Linguagem e framework

- **Linguagem orientada a objetos:** Python 3.12
- **Framework de testes unitários:** pytest **9.0.3**

O pytest atende aos recursos exigidos pelo enunciado:
- **Suítes de teste** — agrupamento por classe/módulo de teste;
- **Categorias de teste** — `markers` (`@pytest.mark.caso1` … `caso5`);
- **Testes parametrizados** — `@pytest.mark.parametrize`;
- **Testes de exceção** — `pytest.raises`.

## Casos de deduplicação implementados

| Caso | Problema | Forma padrão-ouro |
|------|----------|-------------------|
| 1 | Diferenças tipográficas (acento, cedilha, apóstrofo) | grafia acentuada correta |
| 2 | Sobrenome + iniciais (`Seabra A M`) | versão completa do nome |
| 3 | Partícula "de" omitida + ponto opcional | versão completa com "de" |
| 4 | Iniciais agrupadas + sobrenome (`VC Junior`) | versão completa |
| 5 | IDs diferentes para o mesmo autor | menor ID |

## Como executar os testes

Pré-requisitos: Python 3.12+.

```bash
# 1. Criar e ativar o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Instalar as dependências
pip install -r requirements.txt

# 3. Rodar TODOS os testes
pytest

# Rodar com saída detalhada
pytest -v

# Rodar apenas uma categoria (ex.: Caso 1)
pytest -m caso1
```

A barra verde (todos os testes passando) indica as unidades implementadas
corretamente.
