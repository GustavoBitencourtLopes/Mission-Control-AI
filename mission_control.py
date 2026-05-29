nome_da_missao = "Sirius Voyage"
nome_da_equipe = "Equipe Apollo"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# ============================================================
# MATRIZ PRINCIPAL DA MISSÃO
# Ordem:
# [temperatura, comunicacao, bateria, oxigenio, estabilidade]
# ============================================================

dados_da_missao = [

    # CICLO 1
    [22, 96, 93, 98, 95],

    # CICLO 2
    [29, 91, 88, 96, 90],

    # CICLO 3
    [32, 58, 79, 92, 74],

    # CICLO 4
    [35, 49, 43, 87, 61],

    # CICLO 5
    [41, 22, 18, 76, 33]

]

# ============================================================
# FUNÇÕES DE ANÁLISE
# ============================================================

def analisar_temperatura(temperatura):

    if temperatura < 18:
        return "ATENÇÃO"

    elif temperatura <= 30:
        return "NORMAL"

    elif temperatura <= 35:
        return "ATENÇÃO"

    else:
        return "CRÍTICO"


def analisar_comunicacao(comunicacao):

    if comunicacao < 30:
        return "CRÍTICO"

    elif comunicacao <= 59:
        return "ATENÇÃO"

    else:
        return "NORMAL"


def analisar_bateria(bateria):

    if bateria < 20:
        return "CRÍTICO"

    elif bateria <= 49:
        return "ATENÇÃO"

    else:
        return "NORMAL"


def analisar_oxigenio(oxigenio):

    if oxigenio < 80:
        return "CRÍTICO"

    elif oxigenio <= 89:
        return "ATENÇÃO"

    else:
        return "NORMAL"


def analisar_estabilidade(estabilidade):

    if estabilidade < 40:
        return "CRÍTICO"

    elif estabilidade <= 69:
        return "ATENÇÃO"

    else:
        return "NORMAL"


# ============================================================
# FUNÇÃO DE CÁLCULO DE RISCO
# ============================================================

def calcular_pontuacao(status):

    if status == "NORMAL":
        return 0

    elif status == "ATENÇÃO":
        return 1

    else:
        return 2


# ============================================================
# FUNÇÃO DE CLASSIFICAÇÃO DO CICLO
# ============================================================

def classificacao_de_ciclo(pontuacao_total):

    if pontuacao_total <= 2:
        return "MISSÃO ESTÁVEL"

    elif pontuacao_total <= 5:
        return "MISSÃO EM ATENÇÃO"

    else:
        return "MISSÃO CRÍTICA"


# ============================================================
# FUNÇÃO DE RECOMENDAÇÕES AUTOMÁTICAS
# ============================================================

def gerar_recomendacao(
    status_temperatura,
    status_comunicacao,
    status_bateria,
    status_oxigenio,
    status_estabilidade
):

    if (
        status_temperatura == "CRÍTICO" and
        status_bateria == "CRÍTICO" and
        status_oxigenio == "CRÍTICO"
    ):

        return "Ativar protocolo de sobrevivência da missão."

    elif status_temperatura == "CRÍTICO":

        return "Verificar urgentemente o controle térmico."

    elif status_comunicacao == "CRÍTICO":

        return "Restabelecer comunicação com a base."

    elif status_bateria == "CRÍTICO":

        return "Ativar modo de economia de energia."

    elif status_oxigenio == "CRÍTICO":

        return "Acionar suporte emergencial de oxigênio."

    elif status_estabilidade == "CRÍTICO":

        return "Reduzir operações não essenciais."

    else:

        return "Manter monitoramento contínuo da missão."


# ============================================================
# CABEÇALHO DO SISTEMA
# ============================================================

contador_ciclo = 1

print("\n")
print("🚀" + "=" * 58)
print("              MISSION CONTROL AI")
print("=" * 60)

print(f"🛰️ Missão : {nome_da_missao}")
print(f"👨‍🚀 Equipe : {nome_da_equipe}")

print("=" * 60)


# ============================================================
# VARIÁVEIS DE RELATÓRIO FINAL
# ============================================================

soma_temperatura = 0
soma_comunicacao = 0
soma_bateria = 0
soma_oxigenio = 0
soma_estabilidade = 0

soma_risco_total = 0

maior_risco = 0
ciclo_mais_critico = 0

quantidade_ciclos_criticos = 0

risco_temperatura = 0
risco_comunicacao = 0
risco_bateria = 0
risco_oxigenio = 0
risco_estabilidade = 0

quantidade_ciclos = len(dados_da_missao)


# ============================================================
# LOOP PRINCIPAL DA MISSÃO
# ============================================================

for ciclo in dados_da_missao:

    print("\n")
    print("🛰️ " + "=" * 56)
    print(f"          CICLO {contador_ciclo}")
    print("=" * 60)

    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    # ========================================================
    # ANÁLISES
    # ========================================================

    status_temperatura = analisar_temperatura(temperatura)
    status_comunicacao = analisar_comunicacao(comunicacao)
    status_bateria = analisar_bateria(bateria)
    status_oxigenio = analisar_oxigenio(oxigenio)
    status_estabilidade = analisar_estabilidade(estabilidade)

    # ========================================================
    # PONTUAÇÃO
    # ========================================================

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

    # ========================================================
    # RECOMENDAÇÃO
    # ========================================================

    recomendacao = gerar_recomendacao(
        status_temperatura,
        status_comunicacao,
        status_bateria,
        status_oxigenio,
        status_estabilidade
    )

    classificacao_ciclo = classificacao_de_ciclo(
        pontuacao_total
    )

    # ========================================================
    # ACUMULADORES
    # ========================================================

    soma_temperatura += temperatura
    soma_comunicacao += comunicacao
    soma_bateria += bateria
    soma_oxigenio += oxigenio
    soma_estabilidade += estabilidade

    soma_risco_total += pontuacao_total

    risco_temperatura += pontos_temperatura
    risco_comunicacao += pontos_comunicacao
    risco_bateria += pontos_bateria
    risco_oxigenio += pontos_oxigenio
    risco_estabilidade += pontos_estabilidade

    # ========================================================
    # CICLO MAIS CRÍTICO
    # ========================================================

    if pontuacao_total > maior_risco:

        maior_risco = pontuacao_total
        ciclo_mais_critico = contador_ciclo

    # ========================================================
    # CONTAGEM DE CICLOS CRÍTICOS
    # ========================================================

    if classificacao_ciclo == "MISSÃO CRÍTICA":

        quantidade_ciclos_criticos += 1

    # ========================================================
    # EXIBIÇÃO DOS DADOS
    # ========================================================

    print(f"🌡️ Temperatura : {temperatura}°C")
    print(f"📡 Comunicação : {comunicacao}%")
    print(f"🔋 Bateria : {bateria}%")
    print(f"🫁 Oxigênio : {oxigenio}%")
    print(f"⚙️ Estabilidade : {estabilidade}%")

    print("-" * 60)

    print(f"🌡️ Status Temperatura : {status_temperatura}")
    print(f"📡 Status Comunicação : {status_comunicacao}")
    print(f"🔋 Status Bateria : {status_bateria}")
    print(f"🫁 Status Oxigênio : {status_oxigenio}")
    print(f"⚙️ Status Estabilidade : {status_estabilidade}")

    print("-" * 60)

    print(f"📊 Pontuação Total : {pontuacao_total}")
    print(f"🧠 Classificação : {classificacao_ciclo}")

    print("-" * 60)

    print(f"🚨 Recomendação : {recomendacao}")

    contador_ciclo += 1


# ============================================================
# MÉDIAS
# ============================================================

media_temperatura = soma_temperatura / quantidade_ciclos
media_comunicacao = soma_comunicacao / quantidade_ciclos
media_bateria = soma_bateria / quantidade_ciclos
media_oxigenio = soma_oxigenio / quantidade_ciclos
media_estabilidade = soma_estabilidade / quantidade_ciclos

risco_medio = soma_risco_total / quantidade_ciclos


# ============================================================
# TENDÊNCIA DA MISSÃO
# ============================================================

primeiro_risco = 0
ultimo_risco = pontuacao_total

if ultimo_risco > primeiro_risco:

    tendencia = "A missão apresentou tendência de piora."

elif ultimo_risco < primeiro_risco:

    tendencia = "A missão apresentou tendência de melhora."

else:

    tendencia = "A missão permaneceu estável."


# ============================================================
# ÁREA MAIS AFETADA
# ============================================================

lista_riscos = [
    risco_temperatura,
    risco_comunicacao,
    risco_bateria,
    risco_oxigenio,
    risco_estabilidade
]

maior_valor_risco = max(lista_riscos)

indice_maior_risco = lista_riscos.index(
    maior_valor_risco
)

area_mais_afetada = areas_monitoradas[
    indice_maior_risco
]


# ============================================================
# RELATÓRIO FINAL
# ============================================================

print("\n")
print("📋" + "=" * 58)
print("             RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

print(f"🛰️ Missão : {nome_da_missao}")
print(f"👨‍🚀 Equipe : {nome_da_equipe}")

print("=" * 60)

print(f"📦 Quantidade de ciclos : {quantidade_ciclos}")

print("\n📊 MÉDIAS DA MISSÃO")
print("-" * 60)

print(f"🌡️ Temperatura média : {round(media_temperatura, 2)}°C")
print(f"📡 Comunicação média : {round(media_comunicacao, 2)}%")
print(f"🔋 Bateria média : {round(media_bateria, 2)}%")
print(f"🫁 Oxigênio médio : {round(media_oxigenio, 2)}%")
print(f"⚙️ Estabilidade média : {round(media_estabilidade, 2)}%")

print("\n🧠 ANÁLISE GERAL")
print("-" * 60)

print(f"🚨 Ciclo mais crítico : {ciclo_mais_critico}")
print(f"📈 Maior risco : {maior_risco}")
print(f"📊 Risco médio : {round(risco_medio, 2)}")
print(f"⚠️ Ciclos críticos : {quantidade_ciclos_criticos}")

print("\n📉 TENDÊNCIA DA MISSÃO")
print("-" * 60)

print(f"📌 {tendencia}")

print("\n🔥 ÁREA MAIS AFETADA")
print("-" * 60)

print(f"➡️ {area_mais_afetada}")

print("\n")
print("✅ Encerrando sistema Mission Control AI...")
print("=" * 60)

