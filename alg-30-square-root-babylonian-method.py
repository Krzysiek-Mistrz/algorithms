liczba = 49
dokladnosc = 0.5
pierwiastek = liczba / 2
while pierwiastek**2 < liczba - dokladnosc or pierwiastek**2 > liczba + dokladnosc:
    pomocnicza = liczba / pierwiastek
    pierwiastek = (pierwiastek + pomocnicza) / 2
print(pierwiastek)

"""dla 1 obiegu petli
pomocnicza = 2
pierwiastek = 13.25

dla 2 obiegu
pomicnicza = 3.63
pierwiastek = 8.43

dla obiegu 3
pomocnicza = 5.81
pierwiastek = 7.12
"""