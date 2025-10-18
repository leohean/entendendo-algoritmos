# Exercicios

3.1 Suponha que eu forneça uma pilha de chamada como esta:
![](stack.jpeg)

Quais informações você pode retirar baseando-se apenas nesta pilha de chamada?
É possível saber que a primeira função a ser chamada foi a "sauda", ela alocou uma variável "nome" com o valor de "Maggie". Em seguida, ela chamou "sauda 2" passando a variável "nome" como parâmetro.

3.2 Suponha que você acidentalmente escreva uma função recursiva que fique executando infinitamente. Como você viu, seu computador aloca memória na pilha para cada chamada de função. O que acontece com a pilha quando a função recursiva fica executando infinitamente?
A pilha também cresce infinitamente junto com a execução da função, isso pode acabar resultando no esgotamento da memória.