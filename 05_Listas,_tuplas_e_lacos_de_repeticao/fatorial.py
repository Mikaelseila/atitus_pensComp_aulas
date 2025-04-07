def fatorial(numerozin):
 if numerozin == 0:
      return 1
 elif numerozin ==-1:
     return None
 else:
      return numerozin * fatorial(numerozin - 1)

numerozin = int(input("adicione um número: "))
print (fatorial(numerozin))

def test():
 assert fatorial(0) == 1
 assert fatorial(1) == 1
 assert fatorial(2) == 2
 assert fatorial(3) == 6
 assert fatorial(4) == 24
 assert fatorial(5) == 120
 assert fatorial(-1) is None
