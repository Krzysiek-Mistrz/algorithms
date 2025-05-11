liczba = 49
poczatek = 0
koniec = liczba
dokladnosc = 0.05

def pierwiastek(poczatek, koniec, dokladnosc):
    global liczba
    while abs(koniec - poczatek) >= dokladnosc:
        srodek = (koniec + poczatek) / 2
        if srodek ** 2 == liczba:
            return srodek
        elif srodek**2 > liczba:
            koniec = srodek
        else:
            poczatek = srodek
    return (koniec + poczatek) / 2

print(pierwiastek(poczatek, koniec, dokladnosc))