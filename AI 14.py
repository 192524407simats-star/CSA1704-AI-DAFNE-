def ab(v, a, b, m):
    if isinstance(v, int):
        return v
    r = -999 if m else 999
    for x in v:
        n = ab(x, a, b, not m)
        r = max(r, n) if m else min(r, n)
        a, b = max(a, r), min(b, r)
        if a >= b:
            break
    return r

print("Best value:", ab([[3, 5], [6, 9]], -999, 999, True))