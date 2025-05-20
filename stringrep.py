
def repetidas(frase: str) -> bool:
    lista_aux = []
    palavras = frase.lower().split(" ") #quebrar a frase em partes, verificar se tem alguma igual e retornar se é verdadeiro ou falso
    for palavra in palavras:
        if palavra in lista_aux:
            return True
        else:
            lista_aux.append(palavra)
    return False

frase = "Aula de Informática e matéria Artes"

print(repetidas(frase))
