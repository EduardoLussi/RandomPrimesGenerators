from time import time_ns
from random import randint


def LaggedFibonacciGenerator(S, tamanho=256, j=24, k=55, N=1000):
    bitOutput = "1"
    for _ in range(tamanho-1):
        out = (S[j - 1] + S[k - 1]) % N # Calcula próximo número aleatório
        S = S[1:]   # Remove primeiro número da lista
        S.append(out)   # Adiciona o número obtido
        b = out % 2 # Obtém binário
        bitOutput += str(b)
    return bitOutput


# somaTempos = 0
# N = 1446482774680192994161
# tamanho = 40
# j = 24
# k = 55
# for _ in range(1000):
#     S = [randint(2**tamanho, 2**(tamanho+1) - 1) for _ in range(k)]
#     print(S)
#     before = time_ns()
#     LaggedFibonacciGenerator(S, tamanho, j, k, N)
#     somaTempos += (time_ns() - before)
# print((somaTempos/1000)/1e3)

