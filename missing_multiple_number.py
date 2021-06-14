a = [1, 2, 3, 4, 8, 10]
b = [x for x in range(a[0], a[-1] + 1)]
a = set(a)
print(list(a ^ set(b)))