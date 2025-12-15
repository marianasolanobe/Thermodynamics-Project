def imprimir_brayton(resultado):
    print("\n" + "=" * 50)
    print("               CICLO BRAYTON")
    print("=" * 50)

    for i in range(1, 5):
        print(f"\n--- ESTADO {i}")
        print(resultado[f"Estado {i}"])

    print("-" * 50)
    print(f"Trabalho da turbina  : {resultado['W_turbina (kJ/kg)']:.2f} kJ/kg")
    print(f"Trabalho do comp.    : {resultado['W_compressor (kJ/kg)']:.2f} kJ/kg")
    print(f"Calor fornecido      : {resultado['Q_entrada (kJ/kg)']:.2f} kJ/kg")
    print(f"Calor rejeitado      : {resultado['Q_saida (kJ/kg)']:.2f} kJ/kg")
    print("-" * 50)
    print(f"Eficiência térmica   : {resultado['Eficiência térmica']*100:.2f} %")
    print("=" * 50)

