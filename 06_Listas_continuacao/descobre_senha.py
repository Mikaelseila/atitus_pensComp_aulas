corretin = 5
tents = 0
senha = int(input("digite sua senha: "))

while senha != 5:
    corretin = False
    print("senha incorreta, tente novamente")
    tents += 1
    print ("tentativas utilizadas: ", tents)
    senha = int(input("digite sua senha: "))
    
if senha == 5:
 print ("senha correta, miseravi")
