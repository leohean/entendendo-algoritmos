def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i

    return menor_indice

def ordenacaoPorSelecao(arr):
    novoArr = []
    
    for i in range(len(arr)):
        menor = buscaMenor(arr)  # Utilizamos essa função para encontrar o indice do menor elemento
        novoArr.append(arr.pop(menor)) # Adicionamos o menor elemento ao array de ordenação e o removemos do array original

    return novoArr

print(ordenacaoPorSelecao([5, 3, 6, 2, 10]))

#Complexidade de tempo: O(n^2), pois para cada elemento do array precisamos comparar com todos os demais.