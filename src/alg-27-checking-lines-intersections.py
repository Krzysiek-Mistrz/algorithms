def czyPrzecinaja(punkt1, punkt2, punkt3, punkt4):
    if punkt1 == punkt3 or punkt1 == punkt4 or punkt2 == punkt3 or punkt2 == punkt4:
        return True
    else:
        a = (punkt2[1] - punkt1[1]) / (punkt2[0] - punkt1[0])
        b = punkt1[1] - (a*punkt1[0])
        if a*punkt3[0] + b >= punkt3[1] and a*punkt4[0] + b <= punkt4[1]:
            return True
        elif a*punkt3[0] + b <= punkt3[1] and a*punkt4[0] + b >= punkt4[1]:
            return True
    return False
print(czyPrzecinaja([1, 2],[6, 12],[1, 8],[6, 0]))