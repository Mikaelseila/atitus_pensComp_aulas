def soma_pares(numeros: list, alvo: int) -> bool:
    somar = []
    for numero in numeros: #pra cada número na lista, adicione ele na lista somar
        somar.append(numero)

    for n in range(len(somar)): #pra cada numero ao longo da lista somar, se a soma deles for igual ao alvo, retorna True, caso o contrário, ele retorna False.
        for j in range(len(somar)):
            if somar[n] + somar[j] == alvo:
                return True
    return False


def test():
    assert soma_pares([1, 2], 4)
    assert not soma_pares([8], 1)
    assert not soma_pares([8], 10)
    assert soma_pares([3, 4, 6], 9)
    assert soma_pares([3, 4, 6], 7)
