#metoda rekurancyjna:

def schematHorneraRekurencyjnie(wspolczynniki, stopien, x):
    if stopien == 0:
        return wspolczynniki[0]
    else:
        return schematHorneraRekurencyjnie(wspolczynniki, stopien-1, x)*x + wspolczynniki[stopien]

#2x^2 + 3x + 1 = x(2x + 3) + 1
#1 + schematRekurencyjny(wspolczynniki, 1, x)*x
#1 + (schematRekurencyjny(wspolczynniki, 0, x) + 3)*x
#1 + (2*x + 3)*x

#metoda iteracyjna

def schematHorneraIteracyjnie(wspolczynniki, stopien, x):
    if stopien == 0:
        return wspolczynniki[0]
    wynik = wspolczynniki[0]
    for i in range(stopien):
        wynik = wynik*x + wspolczynniki[i+1]
    return wynik

#wynik = (2*x + 3)*x + 1

wspolczynniki = [2, 3, 1]
stopien = 2
x = 2

print(str(schematHorneraIteracyjnie(wspolczynniki, stopien, x)))
print(str(schematHorneraRekurencyjnie(wspolczynniki, stopien, x)))