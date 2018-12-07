# Can I reference x,y here?
# print(x,y)


def funcA(x):
    if (x < 10):
        y = x + 5
    else:
        x = x + 10
    # Can I reference x here?
    # print(x)
    # Can I reference y here?
    print(y)


funcA(12)
# Can I reference x,y here?
# print(x,y)


def funcB(x):
    if (x < 10):
        y = x + 5
    else:
        y = x + 10
    # Can I reference y here?
    print(y)


funcB(12)

globalVar1 = 10
globalVar2 = 15


def funcC(globalVar2):
    globalVar1 = 15
    globalVar2 = globalVar1 + 20


funcC(globalVar2)
# What prints?
print(globalVar1, globalVar2)


def funcD(x):
    for y in range(x):
        pass
    # can I reference y here?
    # print(y)


funcD(10)
