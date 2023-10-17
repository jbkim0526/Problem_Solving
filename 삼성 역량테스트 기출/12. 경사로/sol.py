import sys 
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())

b = [list(map(int,input().split())) for _ in range(n)]


slopes = set()

def checkrow(i):

    d = deque()
    h_before = b[i][0]
    
    if (i,0) not in slopes:
        d.append(h_before)
    
    j = 1
    while j < n:
        h = b[i][j]
        
        # 높이 2이상은 못 건넘
        if abs(h-h_before) > 1:
            return False 
        
        # 높이가 같을 때
        if h == h_before:
            if (i,j) in slopes:
                d.clear()
            else:
                d.append(h)
            j += 1

        # 높이가 높아질 때
        if h > h_before:
            if len(d) >= l:
                d = deque([h])
                slopes.add((i,j))
                j += 1
            else:
                return False 
        else:
            for _ in range(l):
                j += 1
                if b[i][j] == h:
                    
            pass
        h_before = h
    return True



# check row 
for i in range(n):
    check


# check column
for col in zip(*b):
    print(col)

