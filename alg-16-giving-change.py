listaMonet = [1, 2, 5, 11]
cena = 40
monety = []

for i in range(len(listaMonet) - 1, -1, -1):
    while cena - listaMonet[i] >= 0:
        cena -= listaMonet[i]
        monety.append(listaMonet[i])

for j in monety:
    print(str(j) + " ", end=None)