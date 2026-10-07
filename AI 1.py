from collections import deque

def solve(start, goal):
    q = deque([(start, [])])
    seen = {start}

    while q:
        s, path = q.popleft()

        if s == goal:
            return path + [s]

        z = s.index(0)

        for n in [z-3, z+3, z-1, z+1]:
            if 0 <= n < 9:
                a = list(s)
                a[z], a[n] = a[n], a[z]
                a = tuple(a)

                if a not in seen:
                    seen.add(a)
                    q.append((a, path + [s]))

start = (1, 4, 2, 3, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

answer = solve(start, goal)

for s in answer:
    print(s[0], s[1], s[2])
    print(s[3], s[4], s[5])
    print(s[6], s[7], s[8])
    print()
