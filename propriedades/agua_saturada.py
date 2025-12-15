from propriedades.estado import Estado
from propriedades.tabelas import carregar_tabela_a4, carregar_tabela_a5
from propriedades.interpolacao import interp_1d

# carrega tabelas uma vez
df_a4 = carregar_tabela_a4()
df_a5 = carregar_tabela_a5()


# ==================================================
# Água saturada por TEMPERATURA (Tabela A-4)
# ==================================================
def agua_saturada_por_T(T, x):
    estado = Estado(T=T, x=x)

    estado.P = interp_1d(T, df_a4["T"], df_a4["Psat"])

    estado.v = interp_1d(T, df_a4["T"], df_a4["vf"]) + \
               x * (interp_1d(T, df_a4["T"], df_a4["vg"]) -
                    interp_1d(T, df_a4["T"], df_a4["vf"]))

    estado.h = interp_1d(T, df_a4["T"], df_a4["hf"]) + \
               x * (interp_1d(T, df_a4["T"], df_a4["hg"]) -
                    interp_1d(T, df_a4["T"], df_a4["hf"]))

    estado.u = interp_1d(T, df_a4["T"], df_a4["uf"]) + \
               x * (interp_1d(T, df_a4["T"], df_a4["ug"]) -
                    interp_1d(T, df_a4["T"], df_a4["uf"]))

    estado.s = interp_1d(T, df_a4["T"], df_a4["sf"]) + \
               x * (interp_1d(T, df_a4["T"], df_a4["sg"]) -
                    interp_1d(T, df_a4["T"], df_a4["sf"]))

    return estado


# ==================================================
# Água saturada por PRESSÃO (Tabela A-5)
# ==================================================
def agua_saturada_por_P(P_MPa, x):
    """
    Água saturada a partir da pressão (MPa) e título x
    """
    estado = Estado(x=x)

    # MPa → kPa
    P_kPa = P_MPa * 1000
    estado.P = P_kPa

    # ⚠️ AQUI ESTÁ A CORREÇÃO DO KeyError
    estado.T = interp_1d(P_kPa, df_a5["P"], df_a5["Tsat"])

    estado.v = interp_1d(P_kPa, df_a5["P"], df_a5["vf"]) + \
               x * (interp_1d(P_kPa, df_a5["P"], df_a5["vg"]) -
                    interp_1d(P_kPa, df_a5["P"], df_a5["vf"]))

    estado.h = interp_1d(P_kPa, df_a5["P"], df_a5["hf"]) + \
               x * (interp_1d(P_kPa, df_a5["P"], df_a5["hg"]) -
                    interp_1d(P_kPa, df_a5["P"], df_a5["hf"]))

    estado.u = interp_1d(P_kPa, df_a5["P"], df_a5["uf"]) + \
               x * (interp_1d(P_kPa, df_a5["P"], df_a5["ug"]) -
                    interp_1d(P_kPa, df_a5["P"], df_a5["uf"]))

    estado.s = interp_1d(P_kPa, df_a5["P"], df_a5["sf"]) + \
               x * (interp_1d(P_kPa, df_a5["P"], df_a5["sg"]) -
                    interp_1d(P_kPa, df_a5["P"], df_a5["sf"]))

    return estado

