# Estados que queremos cobrir
estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Estados que cada estação abrange
estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])

estacoes_final = set() # Conjunto de estações que cobrem todos os estados que queremos

while estados_abranger:
    melhor_estacao = None       # Estação que cobre o maior número de estados
    estados_cobertos = set()    # Conjunto de estados que a estação cobre e que ainda não abrangemos

    # Loop sobre cada estação e o conjunto(set) dela
    for estacao, estados_por_estacao in estacoes.items():
        # Intersecção entre os estados que ainda precisamos abranger e os da estação atual
        cobertos = estados_abranger & estados_por_estacao 

         # Se o número de estados cobertos pela nova estação é maior do que aqueles que já temos fazemos a troca
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos

    # Adicionamos a melhor estação ao conjunto solução
    estacoes_final.add(melhor_estacao)

    #Retiramos os estados que já cobrimos daqueles que ainda precisamos abranger
    estados_abranger -= estados_cobertos

print(estacoes_final)