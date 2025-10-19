voted = {} # Cria uma tabela hash

def verifica_eleitor(nome):
    if voted.get(nome):
        print("Mande o(a) "+nome+" embora!")
    else:
        voted[nome] = True
        print("Deixe o(a) "+nome+" votar!")

verifica_eleitor("tom")

verifica_eleitor("maria")

verifica_eleitor("mike")
verifica_eleitor("mike")