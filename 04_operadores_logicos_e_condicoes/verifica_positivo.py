numero = int(input("digite um número: "))
def eh_positivo(numero):
    if numero >=0:
        print("o número é positivo")
    else:
        print(eh_negativo(numero))



def eh_negativo(numero):
    if numero <=-1:
        print("o número é negativo")
    else:
        print(eh_positivo(numero))

def test():
 assert eh_positivo(1)
 assert eh_positivo(2)
 assert eh_positivo(10)
 assert not eh_positivo(0)
 assert not eh_positivo(-1)
 assert not eh_positivo(-10)

 assert eh_negativo(-1)
 assert eh_negativo(-2)
 assert eh_negativo(-10)
 assert not eh_negativo(0)
 assert not eh_negativo(1)
 assert not eh_negativo(10)
