def fahrenheit_para_celsius(fah):
    cel = (fah -32) / 1.8 #os graus celsius é o grau fahrenheit - 32 divido por 1.8
    return cel


def celsius_para_fahrenheit(cel):
    fah = (1.8 * cel) + 32 #já fahrenheit é o contrário, são os graus celsius multiplicado por 1.8 e somado com 32
    return fah


def test():
 assert celsius_para_fahrenheit(40) == 104
 assert celsius_para_fahrenheit(-25) == -13

 assert celsius_para_fahrenheit(fahrenheit_para_celsius(30)) == 30
