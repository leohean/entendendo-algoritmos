#4.1 Escreva o código para a função soma, vista anteriormente.

def soma(array):
    if array == []:
        return 0
    else:
        return array[0] + soma(array[1:])

print(soma([1, 2, 3, 4]))