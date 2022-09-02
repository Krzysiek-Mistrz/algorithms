arr = [8, 1, 9, 2, 4, 3]
n = len(arr)
i = 1   #we're starting to compare from the 1 element going back
while i < n:
    value = arr[i]
    j = i - 1
    while j >= 0 and value < arr[j]:
        arr[j + 1] = arr[j]
        """so if the element before our value 
        is bigger than value, then the element after 
        (j + 1) should be assigned with previous ele."""
        j -= 1
    arr[j + 1] = value  #to the end element assign our value
    i += 1
print(arr)