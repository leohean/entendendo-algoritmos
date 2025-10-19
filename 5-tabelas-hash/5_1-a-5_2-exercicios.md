Quais destas funções hash são consistentes?
5.1 f(x) = 1
5.2 f(x) = rand()
5.3 f(x) = proximo_espaco_vazio()
5.4 f(x) = len(x)

R: A única função consiste é a 5.4, pois ela mapeia consistentemente uma mesma string(segundo o seu tamanho) para uma mesma posição, ao mesmo tempo que strings de tamanho diferente ela mapeia para outras posições.