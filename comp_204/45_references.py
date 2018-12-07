def mystery1(a, b):
    temp = a
    a = b
    b = temp


x = 1
y = 2
mystery1(x, y)
print(x, y)

x = [1, 2]
y = [2, 3]
mystery1(x, y)
print(x, y)

x = [1, 2]
y = [2, 3]


def mystery2(a, b):
    a[0] = b
    b[1] = a[1]


mystery2(x, y)

print(x, y)
