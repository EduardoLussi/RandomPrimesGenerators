from random import randint
from time import time_ns


def mdc(a, b):
    while b != 0:
        z = a % b
        a = b
        b = z
    return a


def power(b, m, n):
    resultado = 1

    b = b % n   # Atualiza b se for >= n
    while m > 0:
        # Se m for ímpar, multiplica b com o resultado
        if m % 2 != 0:
            resultado = (resultado * b) % n

        m = m >> 1  # Divide m por 2 por shift right
        b = (b * b) % n

    return resultado


def isPrime(p, n):
    if p < 4:   # Corner cases
        return True

    for i in range(n):
        a = 2 + randint(1, p-3) # Obtém inteiro 2 < a < p
        # Verifica teorema de Fermat mdc(a, p) = 1 e a^(p-1) mod p = 1
        if mdc(a, p) != 1 or power(a, p-1, p) != 1:
            return False    # Não vale, então o número não é primo

    return True # O número é provavelmente primo, P >= 1 - 1/(2^n)


# res = False
# somaTempos = 0
# for _ in range(10):
#     before = time_ns()
#     res = isPrime(651318217807, 8)
#     somaTempos += (time_ns() - before)
# print((somaTempos/10)/1e3)
# print(res)
