def imprimir_rankine(resultado):
    print("\n" + "=" * 50)
    print("               CICLO RANKINE")
    print("=" * 50)

    for i in range(1, 5):
        print(f"\n--- ESTADO {i}")
        print(resultado[f"Estado {i}"])

    print("-" * 50)
    print(f"Trabalho da turbina  : {resultado['W_turbina (kJ/kg)']:.2f} kJ/kg")
    print(f"Trabalho da bomba    : {resultado['W_bomba (kJ/kg)']:.2f} kJ/kg")
    print(f"Calor fornecido      : {resultado['Q_caldeira (kJ/kg)']:.2f} kJ/kg")
    print("-" * 50)
    print(f"Eficiência térmica   : {resultado['Eficiência térmica']*100:.2f} %")
    print("=" * 50)

