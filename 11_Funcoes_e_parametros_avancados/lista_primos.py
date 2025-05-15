def eh_primo(numero: int) -> bool: #este é o primo.py contido nessa mesma pasta
    if numero <= 1:
        return False
    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        else:
            return True


def lista_primos(num: int) -> list:
    lista = [] #lista onde a informação será adicionada
    for x in range (num + 1):
        if eh_primo(x): #ele verifica cada número que está no range
            lista.append(x) #se for primo, ele adiciona na lista, caso contrário: o número vai comprar cigarro
    return lista #retorna a lista completa


def test():
  assert lista_primos(10) == [2, 3, 5, 7]
  assert lista_primos(13) == [2, 3, 5, 7, 11, 13]
  assert lista_primos(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
