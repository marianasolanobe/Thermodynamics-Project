class Estado:
    def __init__(self, T=None, P=None, v=None, u=None, h=None, s=None, x=None):
        self.T = T      # °C ou K
        self.P = P      # kPa
        self.v = v      # m³/kg
        self.u = u      # kJ/kg
        self.h = h      # kJ/kg
        self.s = s      # kJ/(kg·K)
        self.x = x      # título

    def __str__(self):
        linhas = []
        linhas.append("-" * 40)
        linhas.append("ESTADO TERMODINÂMICO")
        linhas.append("-" * 40)

        if self.T is not None:
            linhas.append(f"Temperatura (T)      : {self.T:.2f} °C")
        if self.P is not None:
            linhas.append(f"Pressão (P)          : {self.P:.2f} kPa")
        if self.v is not None:
            linhas.append(f"Volume específico    : {self.v:.6f} m³/kg")
        if self.u is not None:
            linhas.append(f"Energia interna (u)  : {self.u:.2f} kJ/kg")
        if self.h is not None:
            linhas.append(f"Entalpia (h)         : {self.h:.2f} kJ/kg")
        if self.s is not None:
            linhas.append(f"Entropia (s)         : {self.s:.4f} kJ/(kg·K)")
        if self.x is not None:
            linhas.append(f"Título (x)           : {self.x:.4f}")

        linhas.append("-" * 40)
        return "\n".join(linhas)

