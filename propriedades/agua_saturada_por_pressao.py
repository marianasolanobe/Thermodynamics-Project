from propriedades.estado import Estado
from propriedades.tabelas import carregar_tabela_a5
from propriedades.interpolacao import interp_1d

# carrega a tabela uma vez
df_a5 = carregar_tabela_a5()


def agua_saturada_por_P(P, x):
    """
    Água saturada a uma pressão P (kPa) e título x
    """
    estado = Estado(P=P, x=x)

    # temperatura de saturação
    estado.T = interp_1d(P, df_a5["P"], df_a5["Tsat"])

    # volume específico
    vf = interp_1d(P, df_a5["P"], df_a5["vf"])
    vg = interp_1d(P, df_a5["P"], df_a5["vg"])
    estado.v = vf + x * (vg - vf)

    # energia interna
    uf = interp_1d(P, df_a5["P"], df_a5["uf"])
    ug = interp_1d(P, df_a5["P"], df_a5["ug"])
    estado.u = uf + x * (ug - uf)

    # entalpia
    hf = interp_1d(P, df_a5["P"], df_a5["hf"])
    hg = interp_1d(P, df_a5["P"], df_a5["hg"])
    estado.h = hf + x * (hg - hf)

    # entropia
    sf = interp_1d(P, df_a5["P"], df_a5["sf"])
    sg = interp_1d(P, df_a5["P"], df_a5["sg"])
    estado.s = sf + x * (sg - sf)

    return estado
