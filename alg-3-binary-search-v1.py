#im going to search in b[] numbers a[] if the number from a will be in b then print YES
n = int(input())
a = []
for i in range(n):
    number = int(input())
    a.append(number)
m = int(input())
b = []
for j in range(m):
    number = int(input())
    b.append(number)
for k in range(m):
    whether = False
    for l in range(n):
        if a[l] == b[m]:
            whether = True
    if whether:
        print("YES")
    else:
        print("NO")