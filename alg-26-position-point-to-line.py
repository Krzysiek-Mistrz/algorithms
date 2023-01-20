punkt = [5, 10]
prosta = [2, 4]

def polozenie(punkt, prosta):
    if prosta[0]*punkt[0]+prosta[1] > punkt[1]:
        return "pod prosta"
    elif prosta[0]*punkt[0]+prosta[1] < punkt[1]:
        return "nad prosta"
    else:
        return "na prostej"

print(polozenie(punkt, prosta))