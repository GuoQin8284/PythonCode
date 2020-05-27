a = [1,2,3,4]
b = iter(a)
print(next(b))

print(next(b))

print(next(b))
print(next(b))

c = [3*x for x in a if x>2]
print(c)