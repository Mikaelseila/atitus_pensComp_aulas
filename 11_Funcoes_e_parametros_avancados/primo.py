from sympy import false


def eh_primo(numero: int) -> bool:
        if numero <= 1: #se o número for menor ou igual ao 1, ele não é primo
            return False
        if numero > 1:
            for i in range(2, numero): #calcula cada número verdadeiro entre 2 e o número digitado
                if numero % i == 0: #se o resultado da divisão entre o número e o i for 0, ele não é primo
                    return False
            else:
                return True #caso o contrário, ele é um número primo.



def test():
 assert not eh_primo(-1)
 assert not eh_primo(0)
 assert not eh_primo(1)
 assert eh_primo(2)
 assert eh_primo(3)
 assert not eh_primo(4)
 assert eh_primo(5)
