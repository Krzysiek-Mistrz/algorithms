def podstawienie(tekst):
    zaszyfrowane = []
    for i in range(1, len(tekst), 2):
        zaszyfrowane.append(tekst[i]); zaszyfrowane.append(tekst[i - 1])
    if len(tekst) % 2 == 1:
        zaszyfrowane.append(tekst[-1])
    return zaszyfrowane
tekst = "abcdefg"
print("niezaszyfrowane: " + tekst)
zaszyfrowane = ""
for i in podstawienie(tekst):
    zaszyfrowane += i
print("zaszyfrowane: " + zaszyfrowane)