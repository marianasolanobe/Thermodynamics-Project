import os

from ciclos.rankine import ciclo_rankine
from ciclos.brayton import ciclo_brayton
from ciclos.combined import ciclo_combinado

from ciclos.print_rankine import imprimir_rankine
from ciclos.print_brayton import imprimir_brayton
from ciclos.print_combined import imprimir_ciclo_combinado

from propriedades.agua_saturada import agua_saturada_por_P


# ==================================================
# Utilidades de interface
# ==================================================
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER para continuar...")


# ==================================================
# Menu principal
# ==================================================
def menu():
    print("========================================")
    print(" TRABALHO – TERMODINÂMICA I")
    print("========================================")
    print("1 - Consultar propriedades da água (saturada)")
    print("2 - Calcular ciclo Rankine")
    print("3 - Calcular ciclo Brayton")
    print("4 - Calcular ciclo combinado Brayton–Rankine")
    print("0 - Sair")
    print("========================================")


# ==================================================
# Programa principal
# ==================================================
def main():
    while True:
        limpar_tela()
        menu()

        op = input("Escolha uma opção: ").strip()

        # ==============================================
        # 1 – PROPRIEDADES DA ÁGUA
        # ==============================================
        if op == "1":
            try:
                P = float(input("\nPressão (MPa): "))
                x = float(input("Título x (0 a 1): "))

                estado = agua_saturada_por_P(P, x)

                print("\nRESULTADO:")
                print(estado)

            except Exception as e:
                print("\nErro ao calcular propriedades:", e)

            pausar()

        # ==============================================
        # 2 – CICLO RANKINE
        # ==============================================
        elif op == "2":
            try:
                P_c = float(input("\nPressão da caldeira (MPa): "))
                T_c = float(input("Temperatura da caldeira (°C): "))
                P_cond = float(input("Pressão do condensador (MPa): "))

                resultado = ciclo_rankine(P_c, T_c, P_cond)
                imprimir_rankine(resultado)

            except Exception as e:
                print("\nErro no ciclo Rankine:", e)

            pausar()

        # ==============================================
        # 3 – CICLO BRAYTON
        # ==============================================
        elif op == "3":
            try:
                P1 = float(input("\nPressão de entrada (kPa): "))
                T1 = float(input("Temperatura de entrada (K): "))
                rp = float(input("Razão de pressão (P2/P1): "))
                T3 = float(input("Temperatura máxima (K): "))

                resultado = ciclo_brayton(P1, T1, rp, T3)
                imprimir_brayton(resultado)

            except Exception as e:
                print("\nErro no ciclo Brayton:", e)

            pausar()

        # ==============================================
        # 4 – CICLO COMBINADO
        # ==============================================
        elif op == "4":
            try:
                print("\nExecutando ciclo combinado com valores padrão do trabalho...")
                resultado = ciclo_combinado()
                imprimir_ciclo_combinado(resultado)

            except Exception as e:
                print("\nErro no ciclo combinado:", e)

            pausar()

        # ==============================================
        # 0 – SAIR
        # ==============================================
        elif op == "0":
            print("\nEncerrando o programa.")
            break

        else:
            print("\nOpção inválida.")
            pausar()


if __name__ == "__main__":
    main()

