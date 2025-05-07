# Algoritmo Genético para Otimização de Rede Neural

## 📌 Visão Geral
Este projeto implementa um algoritmo genético para otimizar os pesos de uma rede neural simples. O objetivo é evoluir uma população de redes neurais para aproximar-se de um valor de saída desejado (`objetivo = 100`).

## 🧠 Estrutura da Rede Neural
- Arquitetura mínima com duas camadas:
  - Camada oculta com `N` neurônios (configurável)
  - Camada de saída com 1 neurônio

## 🔧 Funcionalidades Principais
### Criação da População
- Gera redes neurais com pesos aleatórios
- Tamanho da população configurável

### Avaliação
- Função de fitness baseada na diferença para o objetivo
- Seleção por torneio dos 2 melhores indivíduos

### Operadores Genéticos
- **Crossover uniforme**: Combina pesos dos pais aleatoriamente
- **Mutação gaussiana**: Adiciona pequenas variações nos pesos

### Visualização
- Gráfico de convergência do fitness por geração

## ⚙️ Parâmetros Ajustáveis
```python
objetivo = 100     # Valor desejado na saída
geracoes = 100     # Número de iterações
neuronio = 100     # Neurônios na camada oculta
tamanho_populacao = 100
taxa_mutacao = 0.1
```

## 📦 Estrutura do Código

| Função                | Descrição                                  |
|-----------------------|-------------------------------------------|
| `Criar_Rede_Neural`   | Inicializa pesos aleatórios               |
| `Feedforward`         | Calcula saída da rede                    |
| `Criar_Populacao`     | Gera população inicial                   |
| `Funcao_De_Aptidao`   | Avalia qualidade da solução              |
| `Avaliar_Populacao`   | Testa todos os indivíduos                |
| `Selecionar_Melhores` | Escolhe os 2 melhores                    |
| `Crossover_Uniforme`  | Recombinação genética                    |
| `Mutacao`            | Aplica mutações na nova geração          |

## 📈 Resultados Esperados

- Melhoria progressiva do fitness ao longo das gerações
- Convergência para valores próximos do objetivo
- Gráfico mostrando a trajetória de aprendizado
