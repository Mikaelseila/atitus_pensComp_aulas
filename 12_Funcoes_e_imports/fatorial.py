def fatorial_rec(n):
    # Com recursividade
     if n == 0: # Caso o número seja 0, retorna 1, abaixo disso ele retorna None
        return 1
     elif n < 0:
        return None
     else:
        return n * fatorial_rec(n - 1) # retorna recursivamente a função (1 * 0 = 1, 2 * 1 = 2, e assim por diante)


def fatorial_non_rec(n):
    # Sem recursividade
    if n == 0:
        return 1
    elif n < 0:
        return None
    result = 1
    for i in range(1, n + 1): # Pra cada número a partir de 1, faça o fatorial (se result for 1 e i for 1, 1 * 1 = 1; 1 * 2 = 2; 2 * 3 = 6, e assim até acabar)
        result = result * i
    return result


# fatorial(5) = 5  * fatorial(4)
# fatorial(4) = 4  * fatorial(3)
# fatorial(3) = 3 * fatorial(2)
# fatorial(2) = 2 * fatorial(1)
# fatorial(1) = 1 * fatorial(0)
# fatorial(0) = 1

assert fatorial_rec(-1) is None
assert fatorial_rec(0) == 1
assert fatorial_rec(1) == 1
assert fatorial_rec(2) == 2
assert fatorial_rec(3) == 6
assert fatorial_rec(4) == 24
assert fatorial_rec(5) == 120

assert fatorial_non_rec(-1) is None
assert fatorial_non_rec(0) == 1
assert fatorial_non_rec(1) == 1
assert fatorial_non_rec(2) == 2
assert fatorial_non_rec(3) == 6
assert fatorial_non_rec(4) == 24
assert fatorial_non_rec(5) == 120
