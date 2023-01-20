tablica = [1, 4, 2, 3, 6, 7, 9, 10]

def podciag(tab):
    dlugosc = len(tab)
    max = -1000
    wskaznik = 0
    for i in range(len(tab)):
        if wskaznik < i:
            wskaznik = i
        while wskaznik < dlugosc - 1 and tab[wskaznik] <= tab[wskaznik + 1]:
            wskaznik += 1
        zmiennaDl = wskaznik - i + 1
        if zmiennaDl > max:
            max = zmiennaDl
        wskaznik = 0
    return max

print(podciag(tablica))