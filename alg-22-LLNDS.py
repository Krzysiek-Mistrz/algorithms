tablica = [1, 7, 2, 1, 8, 9, 4]

dlugosc = [0]*len(tablica)

dlugosc[len(dlugosc)-1]=1

for i in range(len(tablica)-1, -1, -1):
    pom = tablica[i]
    for j in range(i+1, len(tablica), 1):
        if tablica[j] > pom:
            pom = tablica[j]
            dlugosc[i] += 1
    dlugosc[i]+=1

for k in dlugosc:
    print(str(k) + " ", end="")