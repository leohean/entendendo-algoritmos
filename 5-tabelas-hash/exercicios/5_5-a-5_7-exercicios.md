É importante que funções hash tenham uma boa distribuição. Dessa forma, elas ficam com o mapeamento mais amplo possível. O pior caso é uma função hash que mapeia todos os itens para o mesmo espaço da tabela hash.

Suponha que você tenha estas quatro funções hash que operam com strings:

a. Retorne “1” para qualquer entrada.
b. Use o comprimento da string como o índice.
c. Use o primeiro caractere da string como índice. Assim, todas as strings que iniciam com a letra a são hasheadas juntas e assim por diante.
d. Mapeie cada letra para um número primo: a = 2, b = 3, c = 5, d = 7, e = 11, e assim por diante. Para uma string, a função hash é a soma de todos os caracteres–módulo² conforme o tamanho da hash. Se o tamanho de sua hash for 10, por exemplo, e a string for “bag”, o índice será (3 + 2 + 17) % 10 = 22 % 10 = 2.

Para cada um destes exemplos, qual função hash fornecerá uma boa distribuição? Considere que o tamanho da tabela hash tenha dez espaços.

5.5 Uma lista telefônica em que as chaves são os nomes e os valores são os números telefônicos. Os nomes são os seguintes: Esther, Ben, Bob e Dan.
R: A função que fornecerá uma boa distribuição para esse caso é a opção "d".

5.6 Um mapeamento do tamanho de baterias e sua devida potência. Os tamanhos são A, AA, AAA e AAAA.
R: A função que fornecerá uma boa distribuição para esse caso é a opção "b".

5.7 Um mapeamento de títulos de livros e autores. Os títulos são Maus, Fun Home e Watchmen.
R: A função que fornecerá uma boa distribuição para esse caso é a opção "c".