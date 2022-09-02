n = int(input())
a = []
for i in range(n):
    liczba = int(input())
    a.append(liczba)
for j in range(n - 1):
    for k in range(n - j - 1):  #we're going from the beginning to the end
        if a[k] > a[k + 1]:
            a[k], a[k + 1] = a[k + 1], a[k]
print(a)