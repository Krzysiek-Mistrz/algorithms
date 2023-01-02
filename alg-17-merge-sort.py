def sortuj(tablica, poczatek, koniec):
    if koniec > poczatek:
        srodek = (koniec + poczatek) // 2
        sortuj(tablica, poczatek, srodek)
        sortuj(tablica, srodek + 1, koniec)
        scal(tablica, poczatek, srodek, koniec)

def scal(tablica, poczatek, srodek, koniec):
    lewaDlugosc = srodek + 1 - poczatek
    prawaDlugosc = koniec - srodek
    lewaTablica = [0]*lewaDlugosc
    prawaTablica = [0]*prawaDlugosc
    for i in range(lewaDlugosc):
        lewaTablica[i] = tablica[i+poczatek]
    for j in range(prawaDlugosc):
        prawaTablica[j] = tablica[j + srodek + 1]
    wskaznikLewy, wskaznikPrawy, wskaznikGlowny = 0, 0, poczatek
    while wskaznikLewy < lewaDlugosc and wskaznikPrawy < prawaDlugosc:
        if lewaTablica[wskaznikLewy] <= prawaTablica[wskaznikPrawy]:
            tablica[wskaznikGlowny] = lewaTablica[wskaznikLewy]
            wskaznikLewy += 1
        else:
            tablica[wskaznikGlowny] = prawaTablica[wskaznikPrawy]
            wskaznikPrawy += 1
        wskaznikGlowny += 1
    while wskaznikLewy < lewaDlugosc:
        tablica[wskaznikGlowny] = lewaTablica[wskaznikLewy]
        wskaznikGlowny += 1
        wskaznikLewy += 1
    while wskaznikLewy < lewaDlugosc:
        tablica[wskaznikGlowny] = lewaTablica[wskaznikLewy]
        wskaznikGlowny += 1
        wskaznikLewy += 1