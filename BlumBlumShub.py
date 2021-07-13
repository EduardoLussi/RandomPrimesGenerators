from random import randint
from time import time_ns
from MillerRabin import isPrime


def BlumBlumShub(tamanho=256, p=7, q=19, x=randint(1, 132)):
    N = p * q
    numBinario = "1"
    # Gera um número aleatório para cada dígito binário
    for _ in range(tamanho-2):
        b = x % 2   # Obtém bit menos significativo de xi
        numBinario += str(b)
        x = x*x % N # Calcula próximo x
    numBinario += "1"

    return numBinario


# p = 33451251839
# q = 43241513999
# tamanho = 40
#
# before = time_ns()
# x = randint(2**(tamanho-1), 2**tamanho - 1)
# num = int(bytearray(BlumBlumShub(tamanho, p, q, x), "utf8"), 2)
# while isPrime(num, 4) is False:
#     x = randint(2 ** (tamanho - 1), 2 ** tamanho - 1)
#     num = int(bytearray(BlumBlumShub(tamanho, p, q, x), "utf8"), 2)
#
# print((time_ns() - before)/1e3)
# print(num)
