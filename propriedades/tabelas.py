import pandas as pd
from pathlib import Path

def ler_tabela_txt(caminho, colunas):
    """
    Lê tabelas no formato TXT do projeto:
    - separadas por espaço
    - vírgula como decimal
    - ponto como separador de milhar
    """
    return pd.read_csv(
        caminho,
        sep=r"\s+",
        header=None,
        names=colunas,
        decimal=",",
        thousands="."
    )


def carregar_tabela_a4():
    colunas = [
        "T", "Psat",
        "vf", "vg",
        "uf", "ufg", "ug",
        "hf", "hfg", "hg",
        "sf", "sfg", "sg"
    ]
    caminho = Path("tabelas/tabela_A-4.txt")
    return ler_tabela_txt(caminho, colunas)


def carregar_tabela_a5():
    colunas = [
        "P", "Tsat",
        "vf", "vg",
        "uf", "ufg", "ug",
        "hf", "hfg", "hg",
        "sf", "sfg", "sg"
    ]
    caminho = Path("tabelas/tabela_A-5.txt")
    return ler_tabela_txt(caminho, colunas)
