a, b = 4, 3
x, y = 0, 0

while x != 2 and y != 2:
    if x == 0:
        x = a
        print("Fill 4L jug:", x, y)

    elif y == b:
        y = 0
        print("Empty 3L jug:", x, y)

    else:
        p = min(x, b - y)
        x -= p
        y += p
        print("Pour 4L -> 3L:", x, y)
