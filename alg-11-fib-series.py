#metoda 1

#1, 1, 2, 3, 5, 8, 13, ...

"""def fib(b):
    if b <= 2:
        return 1
    else:
        return fib(b-1)+fib(b-2)

print(fib(4))"""

#metoda 2

tablicaFib = [1, 1]

def fib(b):
    global tablicaFib
    if b <= 2:
        return 1
    else:
        for i in range(2, b):
            tablicaFib.append(tablicaFib[i-1] + tablicaFib[tablicaFib[i-2]])
    
fib(4)
print(tablicaFib[4-1])