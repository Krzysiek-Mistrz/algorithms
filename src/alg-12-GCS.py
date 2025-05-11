slowo1 = "alamakota"
slowo2 = "ala"
dlugoscSlowo1 = len(slowo1)
dlugoscSlowo2 = len(slowo2)

tablica = []

for i in range(dlugoscSlowo1+1):
    tablica.append([0]*(dlugoscSlowo2+1))

for i in range(dlugoscSlowo1):
    znakSlowo1 = slowo1[i]
    for j in range(dlugoscSlowo2):
        znakSlowo2 = slowo2[j]
        if znakSlowo1 == znakSlowo2:
            tablica[i+1][j+1] = tablica[i][j] + 1
            continue
        tablica[i+1][j+1] = max(tablica[i+1][j], tablica[i][j+1])

maks = -1000

for i in range(dlugoscSlowo1):
    for j in range(dlugoscSlowo2):
        if maks < tablica[i][j]:
            maks = tablica[i][j]

print(maks + 1)