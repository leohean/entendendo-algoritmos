Este é um pequeno grafo da minha rotina matinal.
![](6_3-exercicio-imagem-1.png)

Ele mostra que não posso tomar café da manhã antes de escovar meus dentes. Então “tomar café da manhã” depende de “escovar os dentes”.

Por outro lado, tomar banho não depende de escovar os dentes, pois posso tomar banho antes de escovar os dentes. A partir desse grafo você pode fazer uma lista relacionando a ordem das atividades da minha rotina matinal.

1.Acordar.
2.Tomar banho.
3.Escovar os dentes.
4.Tomar café da manhã.
Note que “tomar banho” pode ser movido, logo essa lista também é válida:

1.Acordar.
2.Escovar os dentes.
3.Tomar banho.
4.Tomar café da manhã.

6.3 Quanto a estas três listas, marque se elas são válidas ou inválidas.
![](6_3-exercicio-imagem-2.png)
R: Apenas a lista B é válida

6.4 Aqui temos um grafo maior. Faça uma lista válida para ele.

Você poderia dizer que essa lista é, de certa forma, ordenada. Se a tarefa A depende da tarefa B, a tarefa A aparece depois na lista. Isso é chamado de ordenação topológica, e é uma maneira de criar uma lista ordenada a partir de um grafo. Imagine que você esteja planejando um casamento e tenha um grafo enorme de tarefas a serem realizadas. Porém você não sabe nem por onde começar. Assim, uma ordenação topológica do grafo poderia ser feita, e dessa forma, uma lista de tarefas já em ordem seria elaborada.
![](6_4-exercicio-imagem-1.png)
R: Lista para o grafo:
1. Acordar
2. Praticar exercício
3. Tomar banho
4. Trocar de roupa
5. Escovar os dentes
6. Tomar café da manhã
7. Embrulhar o lanche

Suponha que você tenha uma árvore genealógica.
![](6_5-exercicio-imagem-1.png)

Esta árvore é um grafo, pois existem vértices (as pessoas) e arestas, e as arestas apontam para os pais dos vértices. Porém todas as arestas apontam para baixo, pois não faria sentido uma árvore genealógica ter arestas apontando para cima! Seu pai não pode ser o pai do seu avô!
![](6_5-exercicio-imagem-2.png)

Isso é chamado de árvore. Uma árvore é um tipo especial de grafo em que nenhuma aresta jamais aponta de volta.

6.5 Quais desses grafos também são árvores?
R: Os grafos A e C são árvores.