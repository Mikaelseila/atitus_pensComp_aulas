def eh_bissexto(ano): #ele verifica se o ano é bissexto ou não (quando o resto do cálculo é igual a 0)
    return ano % 4 == 0


def proximo_bissexto(ano_presente): #verifica qual é o próximo ano bissexto
    ano = ano_presente 
    while not eh_bissexto(ano): 
        ano += 1
    return ano


def test():
 assert eh_bissexto(0)
 assert eh_bissexto(2020)
 assert eh_bissexto(2024)

 assert not eh_bissexto(1)
 assert not eh_bissexto(2022)
 assert not eh_bissexto(2023)

 assert proximo_bissexto(2024) == 2024
 assert proximo_bissexto(2025) == 2028
 assert proximo_bissexto(2029) == 2032
 assert proximo_bissexto(2020) == 2020
