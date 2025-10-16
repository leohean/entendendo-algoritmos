#4.2 Escreva uma função recursiva que conte o número de itens em uma lista.

def conta_itens(lista):
    if lista == []:
        return 0
    else:
        return 1 + conta_itens(lista[1:])

print(conta_itens([1, 2, 3, 4, 5]))