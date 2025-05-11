slowo1 = "abcdefg"
slowo2 = "gfedcba"

def anagram(slowo):
    slownik = {}
    for znak in slowo:
        slownik[znak] = 0
    for i in slowo:
        slownik[i] += 1
    return slownik

if anagram(slowo1) == anagram(slowo2):
    print("Slowa sa angramami", end=None)