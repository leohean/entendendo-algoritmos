# Criando um grafo
grafo = {}

# Definindo as arestas, os vértices e os respectivos pesos
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

# Criando uma tabela que diz o custo para se chegar em cada nó do grafo a partir do inicio
infinito = float("inf")

custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

# Definindo uma tabela que guarda qual é o melhor nó para se alcançar um determinado vértice do grafo
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

# Array com os nós já visitados
processados = []


def djikstra():
    # Primeiro procuramos o caminho de menor custo
    nodo = ache_no_custo_mais_baixo(custos)

    # Enquanto tivermos nós a serem processados
    while nodo is not None:
        # Pegamos o custo do nó
        custo = custos[nodo]
        # Pegamos os vizinhos deste nó
        vizinhos = grafo[nodo]

        # Para cada um dos vizinhos nós iremos fazer
        for n in vizinhos.keys():
            novo_custo = custo + vizinhos[n]

            # O custo até o nosso nó + o custo até o vizinho é menor?
            if custos[n] > novo_custo:
                # Se sim, atualizamos o custo na tabela e o pai utilizado para chegar até o vizinho
                custos[n] = novo_custo
                pais[n] = nodo
        
        # Dizemos que esse nó já foi processado
        processados.append(nodo)
        # Pegamos o próximo nó
        nodo = ache_no_custo_mais_baixo(custos)

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None

    # Iremos iterar cada nó da tabela de custos
    for nodo in custos:
        custo = custos[nodo]
        # Pegamos o nó com menor custo e que ainda não foi processado
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

djikstra()
print(custos)


