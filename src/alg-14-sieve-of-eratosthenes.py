przedzial = 10

tablica = [False, False] + [True] * (przedzial - 2)

for i in range(2, przedzial):
    wielokrotnosc = 2
    while wielokrotnosc * i < przedzial:
        tablica[wielokrotnosc * i] = False
        wielokrotnosc += 1 # wielokrotnosc = wielokrotnosc + 1

for i in range(len(tablica)):
    print(str(i) + " " + str(tablica[i]))