"""
def merge(a, b):
    c = []
    i, j = 0
    n, m = len(a), len(b)
    while i < n and j < m:
        if a[i] < b[j]:
            c[i + j -1] = a[i]
            i += 1
        else:
            c[i + j -1] = b[j]
            j += 1
    if i == n:
        while j < m:
            c[i + j - 1] = b[j]
            j += 1
    elif j == m:
        while i < n:
            c[i + j - 1] = a[i]
            i += 1
def sort(array, x, y):
    if x > y:
        return []
    if x == y:
        return array[x]
    else:
        mid = (x + y) // 2
        return merge(sort(array, x, mid), sort(array, mid + 1, y))
array = []
n = int(input())
for i in range(n):
    number = int(input())
    array.append(number)
sort(array, 0, len(array) - 1)
"""

def sort(array):
	if len(array) > 1:
		mid = len(array) // 2
        #recursively calling halves of an array
		left = array[:mid]
		right = array[mid:]
		sort(left)
		sort(right)
		i = j = k = 0
		#replace data in array
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				array[k] = left[i]
				i += 1
			else:
				array[k] = right[j]
				j += 1
			k += 1
		#adding left elements
		while i < len(left):
			array[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			array[k] = right[j]
			j += 1
			k += 1
array = []
n = int(input())
for i in range(n):
    number = int(input())
    array.append(number)
sort(array)
print(array)