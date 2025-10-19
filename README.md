# Entendendo Algoritmos

## Introdução a Algoritmos

### Pesquisa Binária
A Pesquisa Binária busca um valor num vetor ordenado (se estiver desordenado não vai funcionar). 

**Para isso ela começa pegando o meio do vetor e pergunta "O número que eu quero é maior ou menor que este valor do meio?"**
Se for maior, nós atualizamos o "baixo" para ser a posição do meio, para assim considerarmos a metade maior.
Porém se for menor, nós atualizamos o alto com a posição do meio e assim começar a olhar a metade inferior do vetor.

E assim sucessivamente até acharmos a posição do número que queremos. Veja a implementação desse algoritmo a seguir:

```
def pesquisa_binaria(lista, item):
	baixo = 0
	alto = len(lista) - 1

while baixo <= alto:
	meio = (baixo + alto) // 2
	chute = lista[meio]

	if chute == item:
		return meio
	if chute > item:
		alto = meio - 1
	else:
		baixo = meio + 1
return None

minha_lista = [1 ,3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))
```

### Big O
A notação Big O nos diz quantas operações um algoritmo vai precisar fazer para resolver um problema no pior caso possível.

Por exemplo, se tivermos um algoritmo O(n²) quer dizer que para uma entrada n, ele fará o quadrado desse número. Já para um outro algoritmo O(log n), ele levará o logaritmo desse n.

Isso é muito para analisarmos o desempenho algoritmos, pois por exemplo enquanto o primeiro algoritmo levaria 1.6 x 10¹⁹  operações, o segundo em 32 já resolveria o problema.

## Ordenação por seleção

### Arrays
Os arrays organizam os dados de forma contígua na memória. Com eles nós conseguimos acessar qualquer posição (acesso aleatório) em O(1). Porém, se quisermos adicionar/deletar um elemento num vetor já criado o custo será O(n), pois precisaremos recriar o vetor inteiro em algum local disponível na memória

### Linked List
As Linked List por sua vez não armazenam os dados de forma sequencial, na verdade um elemento aponta para o próximo que pode estar em alguma posição distante na memória. Isso nos permite inserir e deletar em O(1), porém em contrapartida perdemos o acesso randomico, o que faz com que a operação de leitura seja O(n).

## Recursão

A recursão consiste em criar um algoritmo que irá chamar a si mesmo para resolver o problema.

### Pilha
A pilha é uma estrutura de dados que funciona justamente como uma pilha de pratos, na qual o primeiro prato a ser empilhado vai ser o último a ser desempilhado.

## Quicksort

### Dividir para Conquistar
A estratégia dividir para conquistar consiste em:
1. Conquistar: Definir o caso em que  o problema é pequeno o suficiente para ser resolvido.
2.  Dividir: Quebrar o problema em um problema ainda menor de forma recursiva.

Veja o seguinte exemplo:

Suponha que você seja um fazendeiro que tenha uma área de terra.
Você quer dividir sua fazenda em porções quadradas iguais, sendo que estas porções devem ter o maior tamanho possível.

```
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
```

1. Primeiro definimos os casos bases que são quando o comprimento e largura são multiplos entre si.
2. Em seguida. nós tratamos o caso recursivo que nada mais é que pegar o retangulo que sobrou da divisão quando largura e altura não múltiplos. 

### Algoritmo Quicksort

```
def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivo = array[0]
		menores = [i for i in array[1:] if i <= pivo]
		maiores = [i for i in array[1:] if i > pivo]
		return quicksort(menores) + [pivo] + quicksort(maiores)
```

No Quicksort nós definimos:
1. Caso-base: Quando um vetor for vazio ou só tiver 1 elemento ele não precisa ser ordenado.
2. Caso recursivo:
	1.  Escolhermos um pivô qualquer (no nosso exemplo sempre será o do começo do array)
	2. Colocamos todos os elementos que forem menor que o pivo a esquerda. Já aqueles qu forem maiores nós os colocaremos a direita.

A complexidade desse algoritmo é O(n²), mas ela pode variar dependendo do pivô que nós escolhermos.

### Pior caso Vs Caso Médio
Existem casos em que um algoritmo apesar de não ser otimizado, a ponto de ter um complexidade O(n²), podem não ser tão ruins quanto parecem. Isso porquê O(n²) é para o pior caso possível, mas na verdade na maioria do tempo eles operam numa complexidade mais simples. Esse é o caso do QuickSort.

A complexidade do Quicksort varia dependendo do pivô que nós escolhermos. Vejamos:

Se escolhermos sempre o primeiro elemento, além de ter que verificar cada elemento do array n vezes, nós teremos que repetir isso para todos os números, o que faz com que tenhamos n níveis, resultando numa complexidade O(n²)

![[4_2_2-quicksort-pior-caso.png]]

Porém, se escolhermo um elementos aleatório a cada nível ao invés de sempre ser o primeiro, nós poderemos diminuir a quantidade de nível até log n. De modo que, nós teremos n operações em cada nível e log n níveis, resultando numa complexidade de O(n log n).

![[4_2_1-quicksort-caso-medio.png]]

## Tabelas Hash
As tabelas hash  é uma estrutura que nos permite armazenas na forma chave -> valor. Ela é muito útil, por exemplo, quando precisamos ver um item já existe na nossa lista. Veja o exemplo:

```
voted = {} # Cria uma tabela hash

def verifica_eleitor(nome):
	if voted.get(nome):
		print("Mande o(a) "+nome+" embora!")
	else:
		voted[nome] = True
		print("Deixe o(a) "+nome+" votar!")
  

verifica_eleitor("tom") # Deixe o(a) tom votar!

verifica_eleitor("maria") # Deixe o(a) maria votar!

verifica_eleitor("mike") # Deixe o(a) mike votar!
verifica_eleitor("mike") # Mande o(a) mike embora!
```

[^1]: Neste exemplo, nós primeiro deixamos o eleitor votar e registramos que ele voltou. Caso, ele tente votar de novo, ele será barrado
