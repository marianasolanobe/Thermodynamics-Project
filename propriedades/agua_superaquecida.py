import pandas as pd
import numpy as np
import re
from pathlib import Path
from propriedades.estado import Estado
from propriedades.interpolacao import interp_1d


# ==========================================================
# Cache das tabelas A-6
# ==========================================================
_cache_a6 = {}


# ==========================================================
# Descobre automaticamente as pressões disponíveis
# ==========================================================
def pressoes_disponiveis_a6():
    """
    Lê a pasta tabela_A-6 e retorna as pressões disponíveis (MPa)
    a partir do nome dos arquivos.
    """
    pasta = Path("tabelas/tabela_A-6")
    pressoes = []

    for arquivo in pasta.glob("P_*_MPa.txt"):
        match = re.search(r"P_(.*)_MPa", arquivo.stem)
        if match:
            pressoes.append(float(match.group(1)))

    return sorted(pressoes)


# ==========================================================
# Carregamento da tabela A-6 (robusto)
# ==========================================================
def carregar_tabela_a6(P_MPa):
    """
    Carrega a tabela A-6 (vapor superaquecido) para uma pressão específica.
    P_MPa: pressão em MPa (float)
    """
    if P_MPa in _cache_a6:
        return _cache_a6[P_MPa]

    pasta = Path("tabelas/tabela_A-6")
    arquivo = None

    # encontra o arquivo correspondente à pressão (independente do formato)
    for f in pasta.glob("P_*_MPa.txt"):
        try:
            P_arquivo = float(f.stem.split("_")[1])
            if abs(P_arquivo - P_MPa) < 1e-6:
                arquivo = f
                break
        except ValueError:
            continue

    if arquivo is None:
        raise FileNotFoundError(f"Tabela A-6 não encontrada para P = {P_MPa} MPa")

    colunas = ["T", "v", "u", "h", "s"]

    df = pd.read_csv(
        arquivo,
        sep=r"\s+",
        header=None,
        names=colunas,
        decimal=",",
        thousands="."
    )

    df = df.sort_values("T")

    _cache_a6[P_MPa] = df
    return df


# ==========================================================
# Vapor superaquecido – pressão EXATA da tabela
# ==========================================================
def agua_superaquecida(P_MPa, T):
    """
    Vapor superaquecido a pressão EXATA da tabela A-6
    P_MPa: MPa
    T: °C
    """
    df = carregar_tabela_a6(P_MPa)

    Tmin = df["T"].min()
    Tmax = df["T"].max()

    if T < Tmin or T > Tmax:
        raise ValueError(
            f"T = {T} °C fora do intervalo da tabela A-6 "
            f"para P = {P_MPa} MPa [{Tmin}, {Tmax}]"
        )

    return Estado(
        T=T,
        P=P_MPa * 1000,
        v=interp_1d(T, df["T"], df["v"]),
        u=interp_1d(T, df["T"], df["u"]),
        h=interp_1d(T, df["T"], df["h"]),
        s=interp_1d(T, df["T"], df["s"])
    )


# ==========================================================
# Vapor superaquecido – interpolação ENTRE pressões
# ==========================================================
def agua_superaquecida_PT(P_MPa, T):
    """
    Vapor superaquecido com interpolação entre pressões da A-6
    """
    pressoes = pressoes_disponiveis_a6()

    if P_MPa < pressoes[0] or P_MPa > pressoes[-1]:
        raise ValueError("Pressão fora da faixa da tabela A-6")

    # encontra pressões vizinhas
    P1 = max(p for p in pressoes if p <= P_MPa)
    P2 = min(p for p in pressoes if p >= P_MPa)

    # se a pressão for exatamente uma da tabela
    if P1 == P2:
        return agua_superaquecida(P1, T)

    # carrega as duas tabelas
    df1 = carregar_tabela_a6(P1)
    df2 = carregar_tabela_a6(P2)

    # interpolação em temperatura
    v1 = interp_1d(T, df1["T"], df1["v"])
    v2 = interp_1d(T, df2["T"], df2["v"])

    u1 = interp_1d(T, df1["T"], df1["u"])
    u2 = interp_1d(T, df2["T"], df2["u"])

    h1 = interp_1d(T, df1["T"], df1["h"])
    h2 = interp_1d(T, df2["T"], df2["h"])

    s1 = interp_1d(T, df1["T"], df1["s"])
    s2 = interp_1d(T, df2["T"], df2["s"])

    # interpolação em pressão
    v = np.interp(P_MPa, [P1, P2], [v1, v2])
    u = np.interp(P_MPa, [P1, P2], [u1, u2])
    h = np.interp(P_MPa, [P1, P2], [h1, h2])
    s = np.interp(P_MPa, [P1, P2], [s1, s2])

    return Estado(
        T=T,
        P=P_MPa * 1000,
        v=v,
        u=u,
        h=h,
        s=s
    )

