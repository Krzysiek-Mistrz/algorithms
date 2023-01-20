slowo1 = "abcdefg"
slowo2 = "abcdefghijk"

def ktoreWieksze(slowo1, slowo2):
    for i in range(min(len(slowo1), len(slowo2))):
        if slowo1[i].lower() < slowo2[i].lower():
            return slowo2
        elif slowo1[i].lower() > slowo2[i].lower():
            return slowo1
    if len(slowo1) < len(slowo2):
        return slowo2
    else:
        return slowo1

print(ktoreWieksze(slowo1, slowo2))