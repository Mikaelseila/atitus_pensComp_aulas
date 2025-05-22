"""
Meses sao representados como: 1=Jan, 2=Feb, 3=Mar..
"""

MESES_31_DIAS = [1, 3, 5, 7, 8, 10, 12]
MESES_30_DIAS = [4, 6, 9, 11]


def eh_bissexto(ano: int) -> bool:
    return ano % 4 == 0


def total_dias_no_mes(mes: int, ano: int) -> int:
    if mes in MESES_31_DIAS:
        return 31
    if mes in MESES_30_DIAS:
        return 30
    if eh_bissexto(ano):
        return 29
    return 28


assert total_dias_no_mes(1, 2024) == 31
assert total_dias_no_mes(2, 2024) == 29
assert total_dias_no_mes(3, 2024) == 31
assert total_dias_no_mes(11, 2024) == 30


def formata_data(data: list) -> str:
    dia, mes, ano = data #a data é o dia, mes e o ano citado no assert (inicialmente tentei fazer ao contrário (tipo, data = dia, mes, ano), mas não funcionava .-.)
    return f"{dia}/{mes}/{ano}"




assert formata_data([1, 2, 2024]) == "1/2/2024"
assert formata_data([1, 12, 2024]) == "1/12/2024"


def calcula_diferenca(data1: list, data2: list) -> int:
    dia1, mes1, ano1 = data1 #data1 e data2 tem o mesmo principio do data de formata_data, mas os números separam qual é qual
    dia2, mes2, ano2 = data2

    if (ano1, mes1, dia1) > (ano2, mes2, dia2): 
        dia1, mes1, ano1, dia2, mes2, ano2 = dia2, mes2, ano2, dia1, mes1, ano1

    dias = 0 #quantidade de dias entre uma data e outra

    while (dia1, mes1, ano1) != (dia2, mes2, ano2): #enquanto data1 for diferente de data2, ele fará o seguinte passo-a-passo:

        dia1 += 1 
        if dia1 > total_dias_no_mes(mes1, ano1): #se o dia1 for maior que o total de dias no mês selecionado, ele reseta para 1 e adiciona mais um mês
            dia1 = 1
            mes1 += 1
            if mes1 > 12: #se o mês for dezembro, ao chegar ao dia final, ele reseta para janeiro e adiciona 1 ano a mais
                mes1 = 1
                ano1 += 1
        dias += 1

    return dias






def test():
 # Diferenca em dias entre 2/7/2004 e 27/5/2024 é de 7269 dias
 assert calcula_diferenca([2, 7, 2004], [27, 5, 2024]) == 7269
 # Diferenca entre 27/5/2024 e 2/7/2089 é de 23779 dias
 assert calcula_diferenca([27, 5, 2024], [2, 7, 2004 + 85]) == 23777
 # Diferenca entre 2/7/2004 e 2/7/2089 é de 31047 dias
 assert calcula_diferenca([2, 7, 2004], [2, 7, 2004 + 85]) == 31046
 # A data 27/5/2024 representa 23.409669211195926% entre 2/7/2004 e 2/7/2089


 # Diferenca em dias entre 24/7/1991 e 24/10/2024 é de 12146 dias
 assert calcula_diferenca([24, 7, 1991], [24, 10, 2024]) == 12146
 # Diferenca entre 24/10/2024 e 24/7/2076 é de 18900 dias
 assert calcula_diferenca([24, 10, 2024], [24, 7, 1991 + 85]) == 18901
 # Diferenca entre 24/7/1991 e 24/7/2076 é de 31046 dias
 assert calcula_diferenca([24, 7, 1991], [24, 7, 1991 + 85]) == 31047
 # A data 24/10/2024 representa 39.12259228241963% entre 24/7/1991 e 24/7/2076
