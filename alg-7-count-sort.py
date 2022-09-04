a = []
n = int(input())
#creating a serie
for i in range(n):
    number = int(input())
    a.append(number)
#counting
count = [0] * (max(a) + 1)
for j in range(n):
    count[a[j]] += 1
#creating sorted list
sorted = []
for k in range(max(a) + 1):
    while(count[k]) > 0:
        sorted.append(k)
        count[k] -= 1
print(sorted)