number = input("Escolha o ano:")
int(number) % 4
if int(number) % 4 == 0:
 print ("o ano", number, "é bissexto")
else:
 print ("o ano", number, "não é bissexto")