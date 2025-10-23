from collections import deque

grafo = {} #Inicializa o grafo

#Define as relações entre os elementos
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

def pessoa_e_vendedor(nome):
	return nome[-1] == 'm'

def pesquisa(grafo):
	fila_de_pesquisa = deque() #Cria uma fila dupla
	fila_de_pesquisa += grafo["voce"] #Inicializa com o nó inicial
	verificadas = []
	
	while fila_de_pesquisa:
		pessoa = fila_de_pesquisa.popleft()

		if not pessoa in verificadas: # Se essa pessoa ainda não foi verificada
			if pessoa_e_vendedor(pessoa): # É um vendedor de manga
				print(pessoa + " é um vendedor de manga!")
				return True
			else: # Caso não...
				fila_de_pesquisa += grafo[pessoa] #Adicionamos os seus vizinhos
				verificadas.append(pessoa) #Sinalizamos que ele foi verificado
				
	return False # Retornamos False, se não acharmos a pessoa

pesquisa(grafo)
