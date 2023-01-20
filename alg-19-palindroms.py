def palindrom(slowo):
    polowa = len(slowo) // 2
    czy = True
    for i in range(polowa):
        if slowo[i] != slowo[len(slowo) - 1 - i]:
            czy = False
    return czy

print(palindrom("slowo"))