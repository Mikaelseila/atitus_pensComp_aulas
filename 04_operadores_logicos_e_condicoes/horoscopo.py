mes= int(input("mês:"))

def horoscopo(mes):
    if mes <= 0:
        return ("isso n é um mês, cabeça oca")
    if mes > 0 and mes <= 3:
        return ("signo: Python")        
    elif mes > 4 and mes <= 6:
        return ("signo: Java")
    elif mes > 7 and mes <= 9:
        return ("signo: PHP")
    elif mes > 10 and mes <= 12:
        return ("signo: TypeScript")   
    elif mes > 12:
        return ("isso n é um mês, cabeça oca")    
print (horoscopo(mes))


def test():
 assert horoscopo(1) == "Python"
 assert horoscopo(2) == "Python"

 assert horoscopo(4) == "Java"
 assert horoscopo(6) == "Java"

 assert horoscopo(7) == "PHP"
 assert horoscopo(9) == "PHP"

 assert horoscopo(10) == "TypeScript"
 assert horoscopo(12) == "TypeScript"

assert horoscopo(-1) == "isso n é um mês, cabeça oca"
assert horoscopo(0) == "isso n é um mês, cabeça oca"
assert horoscopo(13) == "isso n é um mês, cabeça oca"
