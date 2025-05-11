slowo = "abcdefghijklmn"
klucz = 16 % 26
def zaszyfruj(slowo, klucz):
    zaszyfrowane = ""
    for i in slowo:
        if chr(ord(i) + klucz) > 'z':
            zaszyfrowane += chr(ord(i) + klucz - 26)
        else:
            zaszyfrowane += chr(ord(i) + klucz)
    return zaszyfrowane
print(zaszyfruj(slowo, klucz))