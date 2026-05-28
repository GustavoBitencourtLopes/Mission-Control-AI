nome_da_missao = "Sirius Voyage"
nome_da_equipe = "Equipe Apollo"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# MATRIZ PRINCIPAL DA MISSÃO
# Ordem:
# [temperatura, comunicacao, bateria, oxigenio, estabilidade]
dados_da_missão = [
    # CICLO 1 
    [22, 96, 93, 98, 95],

    # CICLO 2 
    [29, 91, 88, 96, 90],

    # CICLO 3 
    [32, 58, 79, 92, 74],

    # CICLO 4 
    [35, 49, 43, 87, 61],

    # CICLO 5 
    [41, 22, 18, 76, 33],

    
]

# ------------------------------------------------------------
# FUNÇÃO DE ANÁLISE DA TEMPERATURA
# ------------------------------------------------------------
def analisar_temperatura(temperatura):
    if temperatura < 18:
        return "ATENÇÃO"
    
    elif temperatura <= 30:
        return "NORMAL"
    
    elif temperatura <= 35:
        return "ATENÇÃO"
    
    else:
        return "CRÍTICO"
    
# ------------------------------------------------------------
# FUNÇÃO DE ANÁLISE DA COMUNICAÇÃO
# ------------------------------------------------------------
def analisar_comunicacao(comunicacao):
    if comunicacao < 30:
        return "CRÍTICO"
    
    elif comunicacao <= 59:
        return "ATENÇÃO"
    
    else:
        return "NORMAL"

# ------------------------------------------------------------
# FUNÇÃO DE ANÁLISE DA BATERIA
# ------------------------------------------------------------
def analisar_bateria(bateria):
    if bateria < 20:
        return "CRÍTICO"
    
    elif bateria <= 49:
        return "ATENÇÃO"
    
    else:
        return "NORMAL"
    
# ------------------------------------------------------------
# FUNÇÃO DE ANÁLISE DO OXIGÊNIO
# ------------------------------------------------------------  
def analisar_oxigenio(oxigenio):
    if oxigenio < 80:
        return "CRÍTICO"
    
    elif oxigenio <= 89:
        return "ATENÇÃO"
    
    else:
        return "NORMAL"

# ------------------------------------------------------------
# FUNÇÃO DE ANÁLISE DE ESTABILIDADE 
# ------------------------------------------------------------ 
def analisar_estabilidade(estabilidade):
    if estabilidade < 40:
        return "CRÍTICO"
    
    elif estabilidade <= 69:
        return "ATENÇÃO"
    
    else:
        return "NORMAL"

# ------------------------------------------------------------
# FUNÇÃO DE CÁLCULO DE RISCO
# ------------------------------------------------------------
def calcular_pontuacao(status):
    if status == "NORMAL":
        return 0
    
    elif status == "ATENÇÃO":
        return 1
    
    else:
        return 2

# ------------------------------------------------------------
# FUNÇÃO DE CLASSIFICAÇÃO DO CICLO
# ------------------------------------------------------------
def classificacao_de_ciclo(pontuacao_total):
    if pontuacao_total < 2:
        return "MISSÃO ESTÁVEL"
    
    elif pontuacao_total < 5:
        return "MISSÃO EM ATENÇÃO"
    
    else:
        return  "MISSÃO CRÍTICA"

# ------------------------------------------------------------
# FUNÇÃO DE RECOMENDAÇÕES AUTOMÁTICAS
# ------------------------------------------------------------
def gerar_recomendacao(
        status_temperatura,
        status_comunicacao,
        status_bateria,
        status_oxigenio,
        status_estabilidade
                       ):
    if(
        status_temperatura == "CRÍTICO" and
        status_bateria == "CRÍTICO" and
        status_oxigenio == "CRÍTICO"
    ):
        return "Ativar protocolo de sobrevivência da missão."

    elif(
        status_temperatura == "CRÍTICO"
    ):
        return "Verificar urgentemente o controle térmico."

    elif(
        status_comunicacao == "CRÍTICO"
    ):
        return "Restabelecer comunicação com a base."

    elif(
        status_bateria == "CRÍTICO"
    ):
        return "Ativar modo de economia de energia."
    
    elif(
        status_oxigenio == "CRÍTICO"
    ):
        return "Acionar suporte emergencial de oxigênio."
    
    elif status_estabilidade == "CRÍTICO":

        return "Reduzir operações não essenciais."

    else:

        return "Manter monitoramento contínuo da missão."
    
contador_ciclo = 1

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)

print("Missão:", nome_da_missao)
print("Equipe:", nome_da_equipe)

print("=" * 60)


for ciclo in dados_da_missão:

    print("\n")
    print("=" * 60)
    print("CICLO", contador_ciclo)
    print("=" * 60)


    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    status_temperatura = analisar_temperatura(temperatura)
    status_comunicacao = analisar_comunicacao(comunicacao)
    status_bateria = analisar_bateria(bateria)
    status_oxigenio = analisar_oxigenio(oxigenio)
    status_estabilidade = analisar_estabilidade(estabilidade)
    
    pontos_temperatura = calcular_pontuacao(status_temperatura)
    pontos_comunicacao = calcular_pontuacao(status_comunicacao)
    pontos_bateria = calcular_pontuacao(status_bateria)
    pontos_oxigenio = calcular_pontuacao(status_oxigenio)
    pontos_estabilidade = calcular_pontuacao(status_estabilidade)

    
    pontuacao_total = (
        pontos_temperatura +
        pontos_comunicacao +
        pontos_bateria +
        pontos_oxigenio +
        pontos_estabilidade
    )

    recomendacao = gerar_recomendacao(
        status_temperatura,
        status_comunicacao,
        status_bateria,
        status_oxigenio,
        status_estabilidade
    )

    classificacao_ciclo = classificacao_de_ciclo(pontuacao_total)

    print("----------------------------")

    print("Temperatura:", temperatura)
    print("Comunicação:", comunicacao)
    print("Bateria:", bateria)
    print("Oxigênio:", oxigenio)
    print("Estabilidade:", estabilidade)
    print("Status", status_temperatura)
    print("Status", status_comunicacao)
    print("Status", status_bateria)
    print("Status", status_oxigenio)
    print("Status", status_estabilidade)
    print("Pontuação total do ciclo:", pontuacao_total)
    print("Classificação de cliclo", classificacao_ciclo)
    print("Recomendação:", recomendacao)

    contador_ciclo += 1



