def validador_parenteses(entrada: str) -> bool:
    contagem = 0
    for caractere in entrada:
        if caractere == "(": #se o caractere for um (, adicione 1 na contagem
            contagem += 1
        elif caractere == ")": #se o caractere for um ), subtraia 1 na contagem (ou seja, "()" seria 0+1-1 = 0)
            contagem -= 1
            if contagem < 0: #se
                return False
    return contagem == 0 #se a contagem dos parenteses não seja igual a zero, ele retorna como False (ou seja, "(()" é igual a 1, retornando automáticamente como False.)



def test():
    assert validador_parenteses("()")
    assert validador_parenteses("()()")
    assert validador_parenteses("(())")
    assert validador_parenteses("(()()())")
    assert validador_parenteses("(((())()))")

# Valores inválidos
    assert not validador_parenteses(")")
    assert not validador_parenteses("(")
    assert not validador_parenteses("()(")
    assert not validador_parenteses("()()())")
    assert not validador_parenteses("(((())())")
