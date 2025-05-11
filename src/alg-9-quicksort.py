def quicksort(l, start=0, end=None):
    if end is None:
        end = len(l) - 1
    if start < 0 or end >= len(l) or start >= end:
        return
    p = partition(l, start, end)
    print(l)
    quicksort(l, start, p)
    quicksort(l, p+1, end)

def partition(l, start, end):
    pivot = l[(start + end) // 2] #jako punkt osiowy bierzemy środkowy element ciągu
    print(pivot)
    i = start - 1 #lewy wskaźnik, -1, bo w pierwszym kroku dodajemy 1
    j = end + 1 #prawy wskaźnik
    while True:
        #dopóki element pod lewym wskaźnikiem jest większy od punktu osiowego
        #przesuwamy lewy wskaźnik w prawo
        i += 1
        while l[i] < pivot:
            i += 1
        #dopóki element pod prawym wskaźnikiem jest większy od punktu osiowego
        #przesuwamy prawy wskaźnik w lewo
        j -= 1
        while l[j] > pivot:
            j -= 1
        if i >= j: #jeśli wskaźniki się przeskoczyły, kończymy
            return j
        l[i], l[j] = l[j], l[i] #zamiana elementów miejscami
    return j #zwracamy indeks ostatniego elementu lewej części