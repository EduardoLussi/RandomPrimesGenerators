from random import randint
from time import time_ns


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


def MillerRabin(m, n):
    b = 2 + randint(1, n - 4)    # Escolhe valor aleatório b

    x = power(b, m, n)  # Computa x = b^m mod n

    if x == 1 or x == n - 1:
        return True

    while m != n - 1:
        x = (x * x) % n # Calcula próximo valor de x = x^2 mod n

        m *= 2  # Dobra valor de m

        if x == 1:
            return False
        if x == n - 1:
            return True

    return False


def isPrime(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Encontra valor m que multiplica uma potência de 2 e resulta em n-1
    m = n - 1
    while m % 2 == 0:
        m //= 2

    for i in range(k):  # Realiza teste de Miller-Rabin k vezes
        if MillerRabin(m, n) is False:
            return False

    return True


# res = False
# somaTempos = 0
# for _ in range(10):
#     before = time_ns()
#     res = isPrime(651318217807, 4)
#     somaTempos += (time_ns() - before)
# print((somaTempos/10)/1e3)
# print(res)
