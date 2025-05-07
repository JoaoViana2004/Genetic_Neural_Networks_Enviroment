import matplotlib.pyplot as plt
import numpy as np
import copy

# Cria uma rede neural com pesos aleatórios
def Criar_Rede_Neural(neuronios):
    w1 = np.random.rand(neuronios, 1)
    w2 = np.random.rand(1, neuronios)
    return np.array([w1, w2], dtype=object)

# Realiza o cálculo da rede neural (Feedforward)
def Feedforward(rede, entrada):
    a1 = np.dot(entrada, rede[0].T)
    a2 = np.dot(a1, rede[1].T)
    return a2

# Cria uma população de redes neurais
def Criar_Populacao(tamanho, neuronio):
    return [Criar_Rede_Neural(neuronio) for _ in range(tamanho)]

# Avalia quão boa é uma solução (fitness)
def Funcao_De_Aptidao(saida, objetivo):
    return 100 - abs(saida - objetivo / 2)

# Avalia todos os indivíduos e encontra o melhor
def Avaliar_Populacao(populacao, objetivo):
    pontuacoes = []
    melhor_individuo = None
    melhor_pontuacao = -np.inf
    melhor_saida = None

    for individuo in populacao:
        saida = Feedforward(individuo, objetivo)
        aptidao = Funcao_De_Aptidao(saida, objetivo)
        pontuacoes.append(aptidao)

        if aptidao > melhor_pontuacao:
            melhor_individuo = individuo
            melhor_pontuacao = aptidao
            melhor_saida = saida

    return melhor_individuo, melhor_pontuacao, melhor_saida, pontuacoes

# Seleciona os 2 melhores indivíduos com maior pontuação
def Selecionar_Melhores(populacao, pontuacoes):
    # Transforma possíveis arrays em escalares (caso saída do Feedforward seja array)
    pontuacoes_escaladas = [float(p) if isinstance(p, np.ndarray) else p for p in pontuacoes]

    idx1 = np.argmax(pontuacoes_escaladas)
    melhor1 = populacao[idx1]

    # Zera temporariamente para não pegar o mesmo
    pontuacoes_escaladas[idx1] = -np.inf
    idx2 = np.argmax(pontuacoes_escaladas)
    melhor2 = populacao[idx2]

    return melhor1, melhor2

# Gera filhos por crossover uniforme entre dois pais
def Crossover_Uniforme(pais, num_filhos):
    pai1, pai2 = pais
    filhos = []

    for _ in range(num_filhos):
        filho_w1 = np.where(np.random.rand(*pai1[0].shape) < 0.5, pai1[0], pai2[0])
        filho_w2 = np.where(np.random.rand(*pai1[1].shape) < 0.5, pai1[1], pai2[1])
        filho = np.array([filho_w1, filho_w2], dtype=object)
        filhos.append(filho)

    return filhos

# Aplica mutação nos filhos gerando uma nova população
def Mutacao(filhos, tamanho_populacao, taxa=0.1, intensidade=0.1):
    nova_populacao = []
    while len(nova_populacao) < tamanho_populacao:
        for filho in filhos:
            w1 = np.copy(filho[0])
            w2 = np.copy(filho[1])

            mutar = lambda w: w + np.random.normal(0, intensidade, w.shape) * (np.random.rand(*w.shape) < taxa)
            w1 = mutar(w1)
            w2 = mutar(w2)

            nova_populacao.append(np.array([w1, w2], dtype=object))
            if len(nova_populacao) >= tamanho_populacao:
                break
    return nova_populacao

# ---------- Algoritmo Genético Principal ----------

objetivo = 100     # valor de entrada desejado
geracoes = 100     # número de gerações
neuronio = 100    # número de Neuronios nas Redes, quanto mais neuronios, mais dificuldade
historico = []

# Loop principal de evolução
for geracao in range(geracoes):
    if geracao == 0:
        populacao = Criar_Populacao(100, neuronio)
    else:
        populacao = Mutacao(filhos, 100)

    melhor_individuo, melhor_pontuacao, _, pontuacoes = Avaliar_Populacao(populacao, objetivo)
    pais = Selecionar_Melhores(populacao, pontuacoes)
    filhos = Crossover_Uniforme(pais, 10)

    historico.append(melhor_pontuacao[0])

# Mostra a melhoria da solução ao longo das gerações
plt.plot(historico)
plt.title("Evolução do Algoritmo Genético")
plt.xlabel("Geração")
plt.ylabel("Melhor Aptidão")
plt.grid()
plt.show()
