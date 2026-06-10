import unicodedata

_APOSTROFOS = "`´’‘"


def remover_acentos(texto: str) -> str:
    decomposto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in decomposto if unicodedata.category(c) != "Mn")


def normalizar_apostrofo(texto: str) -> str:
    for variante in _APOSTROFOS:
        texto = texto.replace(variante, "'")
    return texto


def contar_acentos(texto: str) -> int:
    decomposto = unicodedata.normalize("NFD", texto)
    return sum(1 for c in decomposto if unicodedata.category(c) == "Mn")


def colapsar_espacos(texto: str) -> str:
    return " ".join(texto.split())
