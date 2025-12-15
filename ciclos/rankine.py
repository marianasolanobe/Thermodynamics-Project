from propriedades.agua_saturada import agua_saturada_por_P
from propriedades.agua_superaquecida import agua_superaquecida_PT
from propriedades.estado import Estado


def ciclo_rankine(P_caldeira, T_caldeira, P_cond):
    """
    Ciclo Rankine ideal (bomba e turbina isentrópicas)

    Parâmetros:
    P_caldeira : MPa
    T_caldeira : °C
    P_cond     : MPa
    """

    # ==================================================
    # ESTADO 1 – Saída do condensador (líquido saturado)
    # ==================================================
    estado_1 = agua_saturada_por_P(P_cond, x=0.0)

    # ==================================================
    # ESTADO 2 – Saída da bomba (líquido comprimido)
    # h2 ≈ h1 + v1 (P2 - P1)
    # ==================================================
    P1 = estado_1.P            # kPa
    P2 = P_caldeira * 1000     # kPa

    h2 = estado_1.h + estado_1.v * (P2 - P1)

    estado_2 = Estado(
        T=estado_1.T,
        P=P2,
        h=h2,
        v=estado_1.v,
        s=estado_1.s
    )

    # ==================================================
    # ESTADO 3 – Saída da caldeira (vapor superaquecido)
    # ==================================================
    estado_3 = agua_superaquecida_PT(P_caldeira, T_caldeira)

    # ==================================================
    # ESTADO 4 – Saída da turbina (isentropia)
    # s4 = s3, P4 = P_cond
    # ==================================================
    s4 = estado_3.s

    # propriedades de saturação no condensador
    estado_f = agua_saturada_por_P(P_cond, x=0.0)
    estado_g = agua_saturada_por_P(P_cond, x=1.0)

    sf = estado_f.s
    sg = estado_g.s

    if sf <= s4 <= sg:
        x4 = (s4 - sf) / (sg - sf)
        estado_4 = agua_saturada_por_P(P_cond, x=x4)
    else:
        estado_4 = agua_superaquecida_PT(P_cond, estado_3.T)
        estado_4.s = s4

    # ==================================================
    # BALANÇOS DE ENERGIA
    # ==================================================
    W_turb = estado_3.h - estado_4.h
    W_bomba = estado_2.h - estado_1.h
    Q_cal = estado_3.h - estado_2.h

    eficiencia = (W_turb - W_bomba) / Q_cal

    return {
        "Estado 1": estado_1,
        "Estado 2": estado_2,
        "Estado 3": estado_3,
        "Estado 4": estado_4,
        "W_turbina (kJ/kg)": W_turb,
        "W_bomba (kJ/kg)": W_bomba,
        "Q_caldeira (kJ/kg)": Q_cal,
        "Eficiência térmica": eficiencia
    }

