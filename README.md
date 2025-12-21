# Trabalho – Termodinâmica I  
**Universidade de Brasília (UnB)**

---

## Descrição do Projeto

Este projeto foi desenvolvido como parte do trabalho da disciplina **Termodinâmica I** e tem como objetivo a implementação, em linguagem de programação, de um sistema capaz de:

- Consultar propriedades termodinâmicas da **água** e do **ar**
- Resolver os ciclos **Brayton**, **Rankine** e o **ciclo combinado Brayton–Rankine**
- Aplicar **interpolação** quando necessário para propriedades não tabeladas

O código foi inspirado no funcionamento do software **TermoTab** e utiliza tabelas termodinâmicas clássicas, conforme solicitado no enunciado do trabalho.

---

## Requisitos para Execução

### Sistema Operacional
- Linux, Windows ou macOS

### Linguagem
- **Python 3.10 ou superior**

Verifique sua versão com:
```bash
python --version
```

Dependências

O projeto utiliza as seguintes bibliotecas Python:

* NumPy

* Pandas

Instalação das Dependências

Recomenda-se o uso de um ambiente virtual (venv) para evitar conflitos com outras instalações Python.

Criar o ambiente virtual
```bash
python -m venv .venv
```

Ativar o ambiente virtual

Linux / macOS
```bash
source .venv/bin/activate
```

Windows
```bash
.venv\Scripts\activate
```

Instalar as bibliotecas necessárias
```bash
pip install numpy pandas
```

Como Executar o Projeto

Após ativar o ambiente virtual e instalar as dependências, execute o programa principal:

```bash
python main.py
```

O menu interativo será exibido no terminal.

Estrutura do Projeto
```bash
Thermodynamics-Project/
│
├── main.py                     # Menu principal e interação com o usuário
│
├── ciclos/                     # Modelagem dos ciclos termodinâmicos
│   ├── brayton.py              # Ciclo Brayton
│   ├── rankine.py              # Ciclo Rankine
│   ├── combined.py             # Ciclo combinado Brayton–Rankine
│   ├── print_brayton.py        # Impressão formatada do Brayton
│   ├── print_rankine.py        # Impressão formatada do Rankine
│   └── print_combined.py       # Impressão formatada do ciclo combinado
│
├── propriedades/               # Propriedades termodinâmicas
│   ├── agua_saturada.py        # Água saturada
│   ├── agua_superaquecida.py   # Vapor superaquecido
│   ├── ar_gas_ideal.py         # Ar como gás ideal
│   ├── interpolacao.py         # Interpolação linear
│   └── estado.py               # Classe Estado termodinâmico
│
├── tabelas/                    # Tabelas termodinâmicas
│   ├── tabela_A-4.txt          # Água saturada (em função da temperatura)
│   ├── tabela_A-5.txt          # Água saturada (em função da pressão)
│   ├── tabela_A-6/             # Vapor superaquecido
│   └── tabela_A-7/             # Ar (gás ideal)
│
├── README.md                   # Descrição do projeto
└── manual.pdf                  # Manual detalhado de uso
```

Menu Principal

Ao executar o programa, o seguinte menu é apresentado:

```bash
1 - Consultar propriedades da água (saturada)
2 - Calcular ciclo Rankine
3 - Calcular ciclo Brayton
4 - Calcular ciclo combinado Brayton–Rankine
0 - Sair
```

### Funcionalidades do Programa

O programa foi desenvolvido de forma interativa por meio de um menu em terminal, permitindo a consulta de propriedades termodinâmicas e a resolução de ciclos de potência estudados em Termodinâmica I.

#### Opção 1 – Propriedades da água (saturada)

Permite consultar as propriedades da água na região de saturação a partir da pressão e do título (qualidade).
São retornadas automaticamente temperatura, volume específico, energia interna, entalpia, entropia e título.

#### Opção 2 – Ciclo Rankine

Resolve um ciclo Rankine ideal com vapor superaquecido, considerando bomba e turbina isentrópicas.
O programa fornece:

* Estados termodinâmicos do ciclo

* Trabalho da turbina

* Trabalho da bomba

* Calor fornecido

* Eficiência térmica

#### Opção 3 – Ciclo Brayton

Resolve um ciclo Brayton ideal, tratando o ar como gás ideal.
O programa fornece:

* Estados termodinâmicos

* Trabalhos do compressor e da turbina

* Calores de entrada e saída

* Eficiência térmica

#### Opção 4 – Ciclo combinado Brayton–Rankine

Modela um ciclo combinado no qual o calor residual do ciclo Brayton é utilizado em um ciclo Rankine (HRSG ideal).
O programa fornece:

* Vazão mássica de vapor

* Potência individual dos ciclos

* Potência total do sistema

* Eficiência térmica global

O usuário pode utilizar valores padrão ou inserir dados próprios.

### Modelagem Termodinâmica
#### Água

A água é modelada por meio de tabelas termodinâmicas, contemplando:

* Líquido comprimido

* Mistura saturada

* Vapor superaquecido

São obtidas as propriedades: temperatura, pressão, volume específico, energia interna, entalpia, entropia e título (quando aplicável).

#### Ar

O ar é tratado como gás ideal, conforme a modelagem clássica de ciclos Brayton.

### Interpolação Numérica

Quando necessário, é aplicada interpolação linear (polinômio de 1ª ordem), conforme solicitado no enunciado.

### Hipóteses Adotadas

* Regime permanente

* Processos ideais

* Turbinas e compressores isentrópicos

* Perdas desprezadas

### Observações Funcionalidades

O projeto foi desenvolvido com em clareza, organização e coerência física. A interface em terminal foi escolhida para facilitar a avaliação e garantir portabilidade.

Autores 
* Mariana Solano de Brito Elias
* Carlos Henrique De Paiva Munis
