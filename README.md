# Trabalho – Termodinâmica
**Universidade de Brasília (UnB)**

##  Descrição do Projeto

Este projeto foi desenvolvido como parte do trabalho da disciplina **Termodinâmica I** e tem como objetivo implementar, em linguagem de programação, um sistema para:

- Consulta de propriedades termodinâmicas da **água** e do **ar**
- Modelagem e análise dos ciclos **Brayton**, **Rankine** e do **ciclo combinado Brayton–Rankine**
- Aplicação de interpolação linear para obtenção de propriedades fora dos pontos tabelados

O código foi inspirado no funcionamento do software **TermoTab** e utiliza tabelas termodinâmicas clássicas, conforme exigido no enunciado do trabalho.

---

##  Requisitos para Execução

###  Sistema Operacional
- Linux, Windows ou macOS

###  Linguagem
- Python **3.10 ou superior**

Verifique sua versão com:
```bash
python --version

 Dependências

O projeto utiliza as seguintes bibliotecas Python:

numpy

pandas

 Como instalar as dependências

Recomenda-se o uso de um ambiente virtual (venv).

1. Criar o ambiente virtual:
python -m venv .venv

2. Ativar o ambiente virtual:

Linux / macOS

source .venv/bin/activate


Windows

.venv\Scripts\activate

3. Instalar as bibliotecas necessárias:
pip install numpy pandas

 Como Executar o Projeto

Após instalar as dependências, execute o programa principal:

python main.py


O menu interativo será exibido no terminal.

 Estrutura do Projeto
Thermodynamics-Project/
│
├── main.py                     # Programa principal (menu e interação)
│
├── ciclos/                     # Implementação dos ciclos termodinâmicos
│   ├── brayton.py              # Ciclo Brayton
│   ├── rankine.py              # Ciclo Rankine
│   ├── combined.py             # Ciclo combinado Brayton–Rankine
│   ├── print_brayton.py        # Impressão formatada do Brayton
│   ├── print_rankine.py        # Impressão formatada do Rankine
│   └── print_combined.py       # Impressão formatada do ciclo combinado
│
├── propriedades/               # Cálculo de propriedades termodinâmicas
│   ├── agua_saturada.py        # Água saturada
│   ├── agua_superaquecida.py   # Vapor superaquecido
│   ├── ar_gas_ideal.py         # Ar como gás ideal
│   ├── interpolacao.py         # Interpolação linear
│   └── estado.py               # Classe Estado termodinâmico
│
├── tabelas/                    # Tabelas termodinâmicas
│   ├── tabela_A-4.txt          # Água saturada (T)
│   ├── tabela_A-5.txt          # Água saturada (P)
│   ├── tabela_A-6/             # Vapor superaquecido
│   └── tabela_A-7/             # Ar (gás ideal)
│
├── README.md                   # Descrição do projeto
└── manual.pdf                  # Manual de uso do código

 Menu Principal – Funcionalidades

Ao executar o programa, o seguinte menu é apresentado:

1 - Consultar propriedades da água (saturada)
2 - Calcular ciclo Rankine
3 - Calcular ciclo Brayton
4 - Calcular ciclo combinado Brayton–Rankine
0 - Sair

🔹 Opção 1 – Propriedades da água

Permite consultar propriedades da água na região de saturação, a partir da pressão e do título.

🔹 Opção 2 – Ciclo Rankine

Resolve um ciclo Rankine simples com vapor superaquecido, fornecendo:

Estados termodinâmicos

Trabalhos

Calor fornecido

Eficiência térmica

🔹 Opção 3 – Ciclo Brayton

Resolve um ciclo Brayton ideal utilizando ar como gás ideal, fornecendo:

Estados termodinâmicos

Trabalhos do compressor e turbina

Calores

Eficiência térmica

🔹 Opção 4 – Ciclo combinado Brayton–Rankine

Modela um ciclo combinado no qual o calor residual do Brayton é utilizado em um ciclo Rankine (HRSG ideal), fornecendo:

Vazão mássica de vapor

Potência de cada ciclo

Potência total

Eficiência global

O usuário pode optar por usar valores padrão ou inserir dados personalizados.

 Modelagem Termodinâmica

Água:

Líquido comprimido

Mistura saturada

Vapor superaquecido

Ar:

Tratado como gás ideal

Interpolação:

Linear (1ª ordem) quando necessário

Hipóteses:

Regime permanente

Processos ideais (isentropia em turbinas e compressores)

 Resultados

Os resultados obtidos são fisicamente coerentes e compatíveis com valores encontrados na literatura de Termodinâmica, incluindo o artigo de referência da UFRJ utilizado para validação do ciclo combinado.

 Observações Finais

O projeto foi desenvolvido com foco em clareza, organização e robustez

A interface em terminal foi escolhida para garantir portabilidade e fácil avaliação

O código pode ser facilmente estendido para incluir:

Reaquecimento

Regeneração

Eficiências isentrópicas reais

 Autores: Mariana Solona De Brito Elias e Carlos Henrique de Paiva Munis

Trabalho desenvolvido para a disciplina Termodinâmica – UnB.
