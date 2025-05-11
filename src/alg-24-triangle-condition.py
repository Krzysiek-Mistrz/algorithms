boki = [10, 15, 12]

for i in range(len(boki)):
    for j in range(len(boki) - i - 1):
        if boki[j] > boki[j+1]:
            boki[j+1], boki[j] = boki[j], boki[j+1]

ostatni = boki[len(boki)-1]

def warunek(boki):
    global ostatni
    if ostatni < boki[0] + boki[1]:
        return True

print(warunek(boki))