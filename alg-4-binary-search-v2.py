a = []
n = int(input())
for i in range(n):
    liczba = int(input())
    a.append(liczba)
a.sort()
b = []
m = int(input())
for j in range(m):
    liczba = int(input())
    b.append(liczba)
def BinarySearch(x):
    beg = 0
    end = n - 1
    while beg < end:
        mid = (beg + end) // 2
        if x > a[mid]:
            beg = mid + 1
        else:
            end = mid
    return a[beg] == x
for k in range(m):
    if BinarySearch(b[k]):
        print("YES")
    else:
        print("NO") 