import math

a = int(input())

"""def pierwsza(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True"""

def pierwsza(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

print(pierwsza(a))