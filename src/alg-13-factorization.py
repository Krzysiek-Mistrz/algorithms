liczba = int(input())

czynniki = []
czy = True

def rozklad(a):
    global czy
    if a > 1:
        i = 2
        while a != 1:
            if a % i == 0:
                a //= i
                czynniki.append(i)
            else:
                i += 1
    else:
        print("liczba " + str(a) + " nie posiada rozkladu")
        czy = False

rozklad(liczba)

if czy:
    for i in czynniki:
        print(str(i) + " ", end="")