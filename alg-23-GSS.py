tablica = [1, -3, 5, 2, -1, -1, 2, -2, 5, 9, 2]

sumaTeraz = tablica[0]
sumaMax = 0

for i in range(1, len(tablica)):
    if sumaTeraz < 0:
        sumaTeraz = tablica[i]
    else:
        sumaTeraz += tablica[i]
    sumaMax = max(sumaTeraz, sumaMax)

print(str(sumaMax))