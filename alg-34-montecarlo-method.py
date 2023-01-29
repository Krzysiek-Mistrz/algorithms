import random
punktyPoczatek = 100000
punktyKolo = 0
for i in range(punktyPoczatek):
    wspolrzednaX = random.uniform(-1, 1)
    wspolrzednaY = random.uniform(-1, 1)
    if wspolrzednaX**2 + wspolrzednaY**2 <= 1:
        punktyKolo += 1
print(4*punktyKolo / punktyPoczatek)