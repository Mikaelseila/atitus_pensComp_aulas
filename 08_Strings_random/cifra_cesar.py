def caesar_cipher(texto, desvio):
    result = ""
    for char in texto:
        if char.isalpha():
            if char.isupper():
                ascii_offset = 65
            else:
                ascii_offset = 97
            shifted_char = chr((ord(char) - ascii_offset + desvio) % 26 + ascii_offset)
            result += shifted_char
        else:
         result += char
    return result

desvio = 3
texto = "Hello, World!"
print("Original:", texto)

bill_cipher = caesar_cipher(texto, desvio)
print ("Codificado:", bill_cipher)

textin = caesar_cipher(bill_cipher, -desvio)
print("decifradin:", texto)
def test():
 assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"
 assert caesar_cipher("Khoor, Zruog!", -3) == "Hello, World!"

 assert caesar_cipher("Matheus Jardim", 3) == "Pdwkhxv Mduglp"
 assert caesar_cipher("Pdwkhxv Mduglp", -3) == "Matheus Jardim"

 assert caesar_cipher(caesar_cipher("Atitus", 3), -3) == "Atitus"
