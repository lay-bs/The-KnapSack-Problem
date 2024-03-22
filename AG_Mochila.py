from AG_Source import *
from random import getrandbits, randint, random  # depois vai sair

# Definições
peso_item = [30, 10, 3, 25, 75, 10, 2]
peso_maximo_mochila = 100
n_de_cromossomos = 52
geracoes = 95
n_de_itens = len(peso_item)
possivel_melhor_i = 0
possivel_melhor = []
pesagem_possivel_melhor = 0


# Cria a população
populacao = populacao(n_de_cromossomos, n_de_itens)
# print("\n\nPopulação: ", populacao)

for i in range(geracoes):  # gerações
    for x in range(0, n_de_cromossomos):
        pesagem = soma_peso(peso_item, populacao[x])
        if (pesagem > pesagem_possivel_melhor and pesagem <= 100):
            pesagem_possivel_melhor = pesagem
            possivel_melhor_i = x
            possivel_melhor = populacao[x]
            break
    populacao = evolucao(populacao, peso_item, n_de_cromossomos,
                         n_de_itens, peso_maximo_mochila)
    #print("\n\nGeração ", i, " :", populacao)

print("\nItens disponibilizados")
for i in range(n_de_itens):
    print(peso_item[i], "Kg")

print("\nPossível melhor solução: ", possivel_melhor,
      " com ", pesagem_possivel_melhor, "Kg")
