slowo1 = "alamakota" #bedzie wierszem
slowo2 = "ala" #bedzie kolumną
dlugoscSlowo1 = len(slowo1)
dlugoscSlowo2 = len(slowo2)

tablica = []

for i in range(dlugoscSlowo1+1):    #kolumna
    tablica.append([0]*(dlugoscSlowo2+1))   #wiersz

for i in range(dlugoscSlowo1+1):
    tablica[i][0] = 0 # i to kolumna

for i in range(dlugoscSlowo2+1):
    tablica[0][i] = 0 # i to wiersz

for i in range(1, dlugoscSlowo2 + 1):
    for j in range(1, dlugoscSlowo1 + 1):
        if slowo2[i-1] == slowo1[j-1]:
            tablica[j][i] = tablica[j-1][i-1] + 1
        else:
            tablica[j][i] = max(tablica[j-1][i], tablica[j][i-1])

for i in range(dlugoscSlowo2+1):
    for j in range(dlugoscSlowo1+1):
        print(str(tablica[j][i]) + " ", end="")
    print()

"""
for i in range(dlugoscSlowo2+1):
    for j in range(dlugoscSlowo1+1):
        tablica[j][i] = 0
"""
