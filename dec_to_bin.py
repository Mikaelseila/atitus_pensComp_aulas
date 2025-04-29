def dec_to_bin(val):
 resultado = ""
 while val > 0:
  str(val % 2) + resultado
 val >> 1
 return resultado

def bin_to_dec(val):
 pass


 assert dec_to_bin(10) == '1010'
 assert bin_to_dec('1010') == 10