punkt1 = [1, 2]
punkt2 = [3, 6]

punkt = [2, 4]
#a = 2, 
def czyNalezy(punkt1, punkt2, punkt):
    a = (punkt1[1] - punkt2[1]) / (punkt1[0] - punkt2[0])
    b = punkt2[1] - a*punkt2[0]
    if a*punkt[0] + b == punkt[1]:
        if punkt[0] <= punkt2[0] and punkt[0] >= punkt1[0]:
            return True
    return False

print(czyNalezy(punkt1, punkt2, punkt))