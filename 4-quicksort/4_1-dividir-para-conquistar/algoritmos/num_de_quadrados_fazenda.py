#Suponha que você seja um fazendeiro que tenha uma área de terra.
#Você quer dividir sua fazenda em porções quadradas iguais, sendo que estas porções devem ter o maior tamanho possível.

def maior_quadrado_possivel_fazenda(compr, larg):

    if(larg % compr == 0 and larg >= compr):
        return compr
    elif(compr % larg == 0 and compr >= larg):
        return larg
    elif(larg > compr):
        novaLarg = larg % compr
        return maior_quadrado_possivel_fazenda(compr, novaLarg)
    elif(compr > larg):
        novaCompr = compr % larg
        return maior_quadrado_possivel_fazenda(novaCompr, larg)

print(maior_quadrado_possivel_fazenda(640, 1680))