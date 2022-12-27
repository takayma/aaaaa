k, x, y = int(input()), int(input()), int(input())

arr = tuple(range(x, x + k))

arr1 = set({0})
m = 1e+18

while len(arr1) > 0:
	arr2 = set()
	for a in arr1:
		for b in arr:
			if a + b >= y:
				m = min(m, a + b)
				# print(f'm = {m} a + b = {a + b}')
			else:
				arr2.add(a + b)
	# print(arr2)

	arr1 = arr2

print(m)