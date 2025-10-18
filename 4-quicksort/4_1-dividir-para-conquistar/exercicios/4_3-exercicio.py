#4.3 Encontre o valor mais alto em uma lista

def valor_mais_alto(lista):
    if lista == []:
        return 0
    else:
        ret = valor_mais_alto(lista[1:]);

        if lista[0] > ret:
            return lista[0]
        else:
            return ret

lista = [10, 115, 9, 71, 4 , 9, 94, 101]
print(valor_mais_alto(lista))
