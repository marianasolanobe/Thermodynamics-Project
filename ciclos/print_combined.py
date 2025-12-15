def imprimir_ciclo_combinado(res):
    print("\n" + "=" * 50)
    print("        CICLO COMBINADO BRAYTON–RANKINE")
    print("=" * 50)

    print("\n--- DADOS DO SISTEMA")
    print(f"Vazão mássica de ar     : {res['m_dot_ar (kg/s)']:.3f} kg/s")
    print(f"Vazão mássica de vapor  : {res['m_dot_vapor (kg/s)']:.3f} kg/s")

    print("\n--- RESULTADOS DE POTÊNCIA")
    print(f"Potência Brayton        : {res['Potência Brayton (kW)']:.2f} kW")
    print(f"Potência Rankine        : {res['Potência Rankine (kW)']:.2f} kW")
    print(f"Potência total          : {res['Potência Total (kW)']:.2f} kW")

    print("-" * 50)
    print(f"Eficiência global       : {res['Eficiência Global']*100:.2f} %")
    print("=" * 50)

