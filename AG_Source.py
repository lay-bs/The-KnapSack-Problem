from random import getrandbits, randint, random


def cromossomo(n_de_itens):  # geração dos individuos
    return [getrandbits(1) for x in range(n_de_itens)]


def populacao(n_de_individuos, n_de_itens):  # criação da população
    return [cromossomo(n_de_itens) for x in range(n_de_individuos)]


def soma_peso(peso_item, individuo):  # soma os pesos dos itens
    soma = 0
    for i in range(len(peso_item)):
        if (individuo[i] == 1):
            soma += peso_item[i]
    return soma


# validação da pesagem dos individuos
def valida_individuo(peso_item, individuo, capacidade_maxima):
    if (soma_peso(peso_item, individuo) > capacidade_maxima):
        return - 1
    return soma_peso


def mutacao(filho, n_de_itens):  # busca uma posição aleatória da lista do filho e faz a mutação
    indice = randint(0, (n_de_itens - 1))
    if (filho[indice] == 1):
        filho[indice] = 0
    else:
        filho[indice] = 1

    return filho


def crossover(pai, mae, n_de_itens):
    #filho = []
    # faz a divisão da lista ao meio para realizar a troca
    particionamento = n_de_itens // 2
    # filho.append(mutacao((pai[:particionamento] +
    #                      mae[particionamento:]), n_de_itens))
    # filho.append(mutacao((mae[:particionamento] +
    #                      pai[particionamento:]), n_de_itens))
    # filho.append
    return (mutacao((pai[:particionamento] + mae[particionamento:]), n_de_itens))


def verifica_melhores(populacao, peso_maximo_mochila, peso_item):
    # separacao da população para substituir os piores casos
    n = len(populacao)
    validos = []
    invalidos = []
    melhores = []
    pesos_somados = []
    indices = []
    pesos_indices = []

    for i in range(n):
        individuo_peso = soma_peso(peso_item, populacao[i])

        if ((individuo_peso == 0) or individuo_peso > peso_maximo_mochila):
            invalidos.append(populacao[i])
        else:
            validos.append(populacao[i])
            indices.append(i)
            pesos_somados.append(i)

    # retorno dos melhores
    validos_tamanho = len(validos)
    if (validos_tamanho == 2):
        return validos

    elif (validos_tamanho > 2):
        pesos_indices = tuple(zip(indices, pesos_somados))
        melhores = validos
        n_retorno = 2
        first = 0
        last = len(pesos_indices)
        for k in range(0, last):
            for l in range(0, last-k-1):
                if (pesos_indices[l][first] > pesos_indices[l + 1][first]):
                    new_item = pesos_indices[l]
                    pesos_indices[l] = pesos_indices[l + 1]
                    pesos_indices[l + 1] = new_item

        validos_melhores = []
        for i in range(n_retorno):
            x = []
            x = pesos_indices[i]

            y = x[0]
            validos_melhores.append(melhores[y])
        return validos_melhores

    elif (validos_tamanho < 2):
        melhores = validos
        n_retorno = 2 - len(melhores)
        for i in range(n_retorno):
            melhores.append(invalidos[i])
        return melhores

    else:
        return -1  # erro


# faz a evolução da população
def evolucao(populacao, peso_item, n_de_cromossomos, n_de_itens, peso_maximo_mochila):
    invalidos = []  # indice do individuo na população e o peso
    validos = []  # indice do individuo na população e o peso

    # escolha do pai e da mae
    indice_pai = randint(0, n_de_cromossomos-1)
    indice_mae = randint(0, n_de_cromossomos-1)

    # caso ocorra de buscar o mesmo índice para os pais
    while indice_mae == indice_pai:
        indice_pai = randint(0, n_de_cromossomos - 1)

    pai = populacao[indice_pai]
    mae = populacao[indice_mae]

    # geração dos filhos
    filho = crossover(pai, mae, n_de_itens)

    # substituicao dos pais
    pop = (filho, mae, pai)
    melhores = verifica_melhores(pop, peso_maximo_mochila, peso_item)

    if melhores == -1:
        return populacao
    else:
        populacao[indice_pai] = melhores[0]
        populacao[indice_mae] = melhores[1]
        return populacao
