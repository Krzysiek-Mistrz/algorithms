def nwd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def euklides(a, b):
    while a != 0 and b != 0:
        if a > b:
            a-=b
        else:
            b-=a
    return a+b

print(nwd(7, 28))
print(euklides(7, 28))