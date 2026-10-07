def safe(b, r, c):
    for i in range(r):
        if b[i] == c or abs(b[i] - c) == abs(i - r):
            return False
    return True

def solve(b, r):
    if r == 8:
        return True

    for c in range(8):
        if safe(b, r, c):
            b[r] = c
            if solve(b, r + 1):
                return True
    return False

b = [-1] * 8
solve(b, 0)

for r in range(8):
    for c in range(8):
        print("Q" if b[r] == c else "-", end=" ")
    print()
