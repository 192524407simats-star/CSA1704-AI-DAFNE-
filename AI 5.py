from collections import deque
start=(3,3,1); goal=(0,0,0); q=deque([(start,[])])
seen={start}
while q:
    (m,c,b),path=q.popleft()
    if (m,c,b)==goal: print(path+[(m,c,b)]); break
    for x,y in [(1,0),(2,0),(0,1),(0,2),(1,1)]:
        nm,nc=(m-x,c-y) if b else (m+x,c+y)
        nb=1-b
        if 0<=nm<=3 and 0<=nc<=3 and (nm==0 or nm>=nc) and (3-nm==0 or 3-nm>=3-nc):
            s=(nm,nc,nb)
            if s not in seen: seen.add(s); q.append((s,path+[(m,c,b)]))
