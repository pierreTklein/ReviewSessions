x = 5
# This is a comment
# We need a '#' for every line
'''
This is also a comment
This is multilined
'''

# variable comparison
print(5 is 5)
print("Hello" is "Hello")
print(True is False)
print(3 == 3.0)
print('68' == 68)

#Variables
# create and initializaion
y = 10
# look up value
print(y)
# change and reassign
y = "hi"
print(y)

# if vs elif
x = 5
y = 6
z = 7
if x == 5:
    print("x is 5")

if y == 6:
    print("y is 6")
elif x == 5:
    print("x is 5")

if z == 9:
    print("z is 9")
else:
    print("z is not 9")

# nested ifs and equality
a = "a"
b = "b"
c = "c"
if a:
    print(a)
if b == b:
    if 3 == 3.0 and a == 'a':
        print("1")
    if 5 == 6:
        print(1.1)
    else:
        if 4 == 5 or True:
            print(2)
            if not (True and False):
                print("3")
        else:
            print(4)
else:
    print(5)

# nested while loop
i = 0
j = 0
while i < 5:
    while j < i:
        i -= 2
        j += 1
        print(i, j)
    i += 3
print("Finally:", i, j)

# lists vs tuples
list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)

# simple vs compound types
a = 1
b = a
c = a
c = 5

a = [1]
b = a
c = a
c.append(2)

# while duplication list
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = []
i = 0
while i < len(list1):
    list2.append(list1[i])
    i += 1

list2[5] = 10
print(list2, list1)

# for loops
tuple1 = (1, 2, 3, 4, 5)
for t in tuple1:
    print(t)

# loop over indices
list1 = [6, 7, 8, 9, 10]
for l in list1:
    l += 5
print(list1)

list1 = [6, 7, 8, 9, 10]
for i in range(len(list1)):
    list1[i] += 5
    '''
    or alternatively
    old_value = list1[i]
    new_value = old_value + 5
    list1[i] = new_value
    '''
print(list1)

# Reference types and 2D lists
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
list2D = [a, b, c]
a = c
c = b
b = a
a[0] = 'a'
b[1] = 'b'
c[2] = 'c'
a = 6
b = a
a = c[:]
a[2] = 'd'

print(list2D)

# reverse a list composed of lists along order of rows, and order within each row
list2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# we want [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

for line in list2D:
    line.reverse()
list2D.reverse()

print(list2D)

# making some dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {1:1, 2:4, 3:9, 4:16, 5:25}
dict3 = {1: "1", "1": 1, "abc": "def", ("hello world"):"python", True: False}

#dictionaries
dict1 = {1: "1", "1": 1, "abc": "def", "hello": "world", True: False}
for item in dict1:
    print(item)

for key, value in dict1.items():
    print(key, value)

for key in dict1.keys():
    print(key)


# Sets
# iterables
dict1 = {"a": 1, "b": 2, "c": 3}
s = set(dict1)
print(s)
s = set(dict1.items())
print(s)
s = set((1, 2, 3, 3))
print(s)
l = [1, 2, 3, 4, 1, 2, 3, 4]
s = set(l)
print(s)
# does not work
# s = set(5)
# s = set("1", 4, True)

s = {1, 1.0}
print(s)
s = set([2, False, 0])
print(s)
s = set([1, 1.0, True, 0, False])
print(s)

#Sets continued
record = [(1, "A"), (2, "B"), (3, "C"), (2, "C"), (4, "A"), (1, "B"), (1, "C")]

ids = set([r[0] for r in record])

diseases = set()
for id, disease in record:
    diseases.add(disease)

has_A = set()
has_B = set()
has_C = set()
for id, disease in record:
    if disease == "A":
        has_A.add(id)
    if disease == "B":
        has_B.add(id)
    if disease == "C":
        has_C.add(id)
only_C = has_C - has_B - has_A

print(has_A, has_B, has_C, only_C)