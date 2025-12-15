from propriedades.estado import Estado
import math

# constantes do ar (gás ideal)
R = 0.287      # kJ/kg.K
cp = 1.004     # kJ/kg.K
cv = 0.717     # kJ/kg.K
k = 1.4


def ciclo_brayton(P1, T1, rp, T3):
    """
    Ciclo Brayton ideal (compressor e turbina isentrópicos)

    Parâmetros:
    P1 : pressão de entrada (kPa)
    T1 : temperatura de entrada (K)
    rp : razão de pressão (P2/P1)
    T3 : temperatura máxima após combustão (K)
    """

    # ==================================================
    # ESTADO 1 – Entrada do compressor
    # ==================================================
    estado_1 = Estado(
        T=T1,
        P=P1,
        h=cp * T1,
        u=cv * T1,
        s=None,
        v=R * T1 / P1
    )

    # ==================================================
    # ESTADO 2 – Saída do compressor (isentropia)
    # ==================================================
    P2 = P1 * rp
    T2 = T1 * (rp)**((k - 1) / k)

    estado_2 = Estado(
        T=T2,
        P=P2,
        h=cp * T2,
        u=cv * T2,
        s=None,
        v=R * T2 / P2
    )

    # ==================================================
    # ESTADO 3 – Saída da combustão (pressão constante)
    # ==================================================
    estado_3 = Estado(
        T=T3,
        P=P2,
        h=cp * T3,
        u=cv * T3,
        s=None,
        v=R * T3 / P2
    )

    # ==================================================
    # ESTADO 4 – Saída da turbina (isentropia)
    # ==================================================
    P4 = P1
    T4 = T3 * (1 / rp)**((k - 1) / k)

    estado_4 = Estado(
        T=T4,
        P=P4,
        h=cp * T4,
        u=cv * T4,
        s=None,
        v=R * T4 / P4
    )

    # ==================================================
    # BALANÇOS DE ENERGIA
    # ==================================================
    W_turb = estado_3.h - estado_4.h
    W_comp = estado_2.h - estado_1.h
    Q_in = estado_3.h - estado_2.h
    Q_out = estado_4.h - estado_1.h

    eficiencia = (W_turb - W_comp) / Q_in

    return {
        "Estado 1": estado_1,
        "Estado 2": estado_2,
        "Estado 3": estado_3,
        "Estado 4": estado_4,
        "W_turbina (kJ/kg)": W_turb,
        "W_compressor (kJ/kg)": W_comp,
        "Q_entrada (kJ/kg)": Q_in,
        "Q_saida (kJ/kg)": Q_out,
        "Eficiência térmica": eficiencia
    }

