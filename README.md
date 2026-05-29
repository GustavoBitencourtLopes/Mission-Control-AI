🚀 Mission Control AI

Sistema de monitoramento inteligente de missão espacial desenvolvido em Python.

O projeto simula o acompanhamento de indicadores críticos de uma missão espacial, realizando análises automáticas, cálculo de risco, classificação da missão e geração de recomendações operacionais.

📋 Objetivo

Desenvolver um sistema capaz de monitorar diferentes áreas de uma missão espacial e identificar situações de risco através da análise dos dados coletados em cada ciclo operacional.

⚙️ Funcionalidades
Monitoramento de temperatura interna
Monitoramento da comunicação com a base
Monitoramento do sistema de energia
Monitoramento do suporte de oxigênio
Monitoramento da estabilidade operacional
Classificação automática dos indicadores
Cálculo de pontuação de risco
Classificação geral de cada ciclo
Geração de recomendações automáticas
Identificação do ciclo mais crítico
Cálculo de médias da missão
Identificação da área mais afetada
Relatório final da missão
🧠 Conceitos de Python Utilizados

Durante o desenvolvimento foram utilizados:

Variáveis
Listas
Matrizes
Funções
Estruturas condicionais (if, elif, else)
Estruturas de repetição (for)
Acumuladores
Contadores
Operadores lógicos (and)
Cálculo de médias
Manipulação de listas
🛰️ Estrutura dos Dados

Cada ciclo da missão é representado por uma lista contendo:

[
    temperatura,
    comunicacao,
    bateria,
    oxigenio,
    estabilidade
]

Exemplo:

[22, 96, 93, 98, 95]
📊 Classificação de Risco
Temperatura
Faixa	Status
< 18	Atenção
18 a 30	Normal
31 a 35	Atenção
> 35	Crítico
Comunicação
Faixa	Status
< 30	Crítico
30 a 59	Atenção
≥ 60	Normal
Bateria
Faixa	Status
< 20	Crítico
20 a 49	Atenção
≥ 50	Normal
Oxigênio
Faixa	Status
< 80	Crítico
80 a 89	Atenção
≥ 90	Normal
Estabilidade
Faixa	Status
< 40	Crítico
40 a 69	Atenção
≥ 70	Normal
🚨 Classificação da Missão
Pontuação	Resultado
0 a 2	Missão Estável
3 a 5	Missão em Atenção
6 ou mais	Missão Crítica
▶️ Como Executar

Clone o repositório:

git clone https://github.com/SEU-USUARIO/Mission-Control-AI.git

Entre na pasta:

cd Mission-Control-AI

Execute:

python mission_control.py
👨‍🚀 Equipe

Equipe Apollo

🛰️ Missão Simulada

Sirius Voyage

📚 Aprendizados

Este projeto permitiu praticar conceitos fundamentais de programação em Python, incluindo estruturas de dados, lógica de programação, modularização através de funções e análise automatizada de informações.

 Autores

Gustavo Bitencourt RM 568885 e Daniel Vieira RM 573326
