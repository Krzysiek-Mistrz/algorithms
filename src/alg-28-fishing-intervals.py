przedzial = [-7, 4]
#f(x) = 2*x + 4
a = przedzial[0]
b = przedzial[1]
dokladnoscX = dokladnoscY = 0.05

def wartoscFunkcji(x):
    return (2 * x) + 4

def polowanieMiejscZerowych(poczatek, koniec, dokladnoscX, dokladnoscY):
    while abs(koniec - poczatek) >= dokladnoscX:
        srodek = (koniec + poczatek) / 2
        if abs(wartoscFunkcji(srodek)) < dokladnoscY:
            break
        elif wartoscFunkcji(poczatek)*wartoscFunkcji(srodek) < 0:
            koniec = srodek
        else:
            poczatek = srodek
    return (poczatek + koniec) / 2
    
print(polowanieMiejscZerowych(a, b, dokladnoscX, dokladnoscY))