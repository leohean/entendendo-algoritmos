# Exercícios

2.1 Suponha que você esteja criando um aplicativo para acompanhar as suas finanças.

Todos os dias você anotará tudo o que gastou e onde gastou. No final do mês, você deverá revisar os seus gastos e resumir o quanto gastou. Logo, você terá um monte de inserções e poucas leituras.
Você deverá usar um array ou uma lista para implementar este aplicativo?
R: Pelo fato de eu não saber quantas anotações eu vou fazer e também que serão feitas poucas leituras, eu implementaria utilizando uma lista.

2.2 Suponha que você esteja criando um aplicativo para anotar os pedidos dos clientes em um restaurante. Seu aplicativo precisa de uma lista de pedidos. Os garçons adicionam os pedidos a essa lista e os chefs retiram os pedidos da lista. Funciona como uma fila. Os garçons colocam os pedidos no final da fila e os chefs retiram os pedidos do começo dela para cozinhá-los.
Você usaria um array ou uma lista encadeada para implementar essa lista? (Dica: listas encadeadas são boas para inserções/eliminação e arrays são bons para acesso aleatório. O que fazer neste caso?)
R: Eu usaria uma lista encadeada, pois as operações da lista para adição e deleção (importantes no contexto do restaurante) são mais rápidas.

2.3 Vamos analisar um experimento. Imagine que o Facebook guarda uma lista de usuários. Quando alguém tenta acessar o Facebook, uma busca é feita pelo nome de usuário. Se o nome da pessoa está na lista, ela pode continuar o acesso. As pessoas acessam o Facebook com muita frequência, então existem muitas buscas nessa lista. Presuma que o Facebook usa a pesquisa binária para procurar um nome na lista. A pesquisa binária requer acesso aleatório — você precisa ser capaz de acessar o meio da lista de nomes instantaneamente. Sabendo disso, você implementaria essa lista como array ou uma lista encadeada?
R: Eu implementaria utilizando um array, pois a lista encadeada (diferente do array) não oferece acesso aleatório.

2.4 As pessoas se inscrevem no Facebook com muita frequência também. Suponha que você decida usar um array para armazenar a lista de usuários. Quais as desvantagens de um array em relação às inserções? Em particular, imagine que você está usando a pesquisa binária para buscar os logins. O que acontece quando você adiciona novos usuários em um array?
R: O problema do array em relação a novas inserções é que no caso de precisarmos adicionar um novo elemento, no meio por exemplo, precisamos deslocar no pior dos casos todos os demais.

2.5 Na verdade, o Facebook não usa nem arrays nem listas encadeadas para armazenar informações. Vamos considerar uma estrutura de dados híbrida: um array de listas encadeadas. Você tem um array com 26 slots. Cada slot aponta para uma lista encadeada. Por exemplo, o primeiro slot do array aponta para uma lista encadeada que contém os usuários que começam com a letra A. O segundo slot aponta para a lista encadeada que contém os usuários que começam com a letra B, e assim por diante.
Suponha que o Adit B se inscreva no Facebook e você queira adicioná-lo à lista. Você vai ao slot 1 do array, a seguir para a lista encadeada do slot 1, e adiciona Adit B no final. Agora, suponha que você queira procurar o Zakhir H. Você vai ao slot 26, que aponta para a lista encadeada de todos os nomes começados em Z. Então, procura pela lista até encontrar o Zakhir H.
Compare esta estrutura híbrida com arrays e listas encadeadas. É mais lento ou mais rápido fazer inserções e eliminações nesse caso? Você não precisa responder dando o tempo de execução Big(O), apenas diga se a nova estrutura de dados é mais rápida ou mais lenta do que os arrys e as listas encadeadas.
R: A nova estrutura é mais rápida para realizar buscas comparada a lista encadeada, pois permite acesso aleatório pela primeira letra do nome. Além do que também nos permite inserir e/ou deletar elementos sem precisar movimentar os já existentes.