import sys 
from collections import deque
input = sys.stdin.readline

b = [None]
for _ in range(4):
    s = input()[:-1]
    d = deque()
    for c in s:
        d.append(int(c))
    b.append(d)

k = int(input()[:-1])
commands = []
for _ in range(k):
    commands.append(tuple(map(int,input().split())))

scores = [[0,1],[0,2],[0,4],[0,8]]

def rotate(i,direction):
    if direction == 1:
        b[i].appendleft(b[i].pop())
    else:
        b[i].append(b[i].popleft())

# i < j
def checkSame(i,j):
    return b[i][2] == b[j][6]


for i, direction in commands:
    need_rotate = [(i,direction)]
    cur_d = direction
    for j in range(i+1,5):
        if checkSame(j-1,j):
            break 
        cur_d = -cur_d
        need_rotate.append((j,cur_d))

    cur_d = direction
    for j in range(i-1,0,-1):
        if checkSame(j,j+1):
            break 
        
        cur_d = -cur_d
        need_rotate.append((j,cur_d))
        
    for j,rot_dir in need_rotate:
        rotate(j,rot_dir)

ans = 0
for i in range(4):
    ans += scores[i][b[i+1][0]]
print(ans)
