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

    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos

    estacoes_final.add(melhor_estacao)
    estados_abranger -= estados_cobertos

print(estacoes_final)