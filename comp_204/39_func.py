def makeCoord(x, y):
    return (x, y)


def squareCoords(width):
    startX = 0
    startY = 0
    c1 = makeCoord(startX, startY)
    c2 = makeCoord(startX + width, startY)
    c3 = makeCoord(startX + width, startY + width)
    c4 = makeCoord(startX, startY + width)
    return (c1, c2, c3, c4)


print(squareCoords(10))
# Outputs ((0, 0), (10, 0), (10, 10), (0, 10))

a, b, c, d = squareCoords(10)
# What is a,b,c,d?
