a = int(input())
n = int(input())
def power(a, n):
	result = 1
	for i in range(1, n + 1):
		result = result*a 
	return result
print(power(a, n))
"""
exp: a = 5, n = 3 -> 
result = 5 * 1 = 5 -> 
result = 5 * 5 = 25 ->
result = 5 * 25 ->
result = 125
"""