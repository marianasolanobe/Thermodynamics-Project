from ciclos.brayton import ciclo_brayton
from ciclos.rankine import ciclo_rankine


def ciclo_combinado(
    # Brayton
    P1_ar=100,       # kPa
    T1_ar=300,       # K
    rp=10,           # razão de pressão
    T3_ar=1400,      # K

    # Rankine
    P_caldeira=8.0,  # MPa
    T_caldeira=600,  # °C
    P_cond=0.1       # MPa
):
    """
    Ciclo combinado Brayton–Rankine (HRSG ideal)
    """

    # ==================================================
    # 1) Ciclo Brayton
    # ==================================================
    br = ciclo_brayton(
        P1=P1_ar,
        T1=T1_ar,
        rp=rp,
        T3=T3_ar
    )

    Q_out_brayton = br["Q_saida (kJ/kg)"]   # por kg de ar

    # ==================================================
    # 2) Ciclo Rankine
    # ==================================================
    rk = ciclo_rankine(
        P_caldeira=P_caldeira,
        T_caldeira=T_caldeira,
        P_cond=P_cond
    )

    Q_in_rankine = rk["Q_caldeira (kJ/kg)"]  # por kg de vapor

    # ==================================================
    # 3) Acoplamento (HRSG)
    # m_dot_ar * Q_out_B = m_dot_v * Q_in_R
    # assume m_dot_ar = 1 kg/s
    # ==================================================
    m_dot_ar = 1.0  # kg/s
    m_dot_v = (m_dot_ar * Q_out_brayton) / Q_in_rankine

    # ==================================================
    # 4) Potências e eficiência global
    # ==================================================
    W_B = br["W_turbina (kJ/kg)"] - br["W_compressor (kJ/kg)"]
    W_R = rk["W_turbina (kJ/kg)"] - rk["W_bomba (kJ/kg)"]

    W_total = m_dot_ar * W_B + m_dot_v * W_R

    # calor externo entra apenas no Brayton
    Q_externo = br["Q_entrada (kJ/kg)"] * m_dot_ar

    eficiencia_global = W_total / Q_externo

    return {
        "Brayton": br,
        "Rankine": rk,
        "m_dot_ar (kg/s)": m_dot_ar,
        "m_dot_vapor (kg/s)": m_dot_v,
        "Potência Brayton (kW)": m_dot_ar * W_B,
        "Potência Rankine (kW)": m_dot_v * W_R,
        "Potência Total (kW)": W_total,
        "Eficiência Global": eficiencia_global
    }

