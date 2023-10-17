import sys 
from collections import deque
input = sys.stdin.readline

n = int(input())
num_apple = int(input())
apples = [tuple(map(int,input().split()))  for _ in range(num_apple)]
num_d = int(input())
change_dir = deque([tuple(input().split())  for _ in range(num_d)])

snakes = deque()
snakes.append((1,1))
cur_d = 0
directions = [(0,1),(1,0),(0,-1),(-1,0)]

for time in range(1,10001):    
    i,j = snakes[0]
    di,dj = directions[cur_d]
    ni,nj = i+di, j+dj

    # 몸에 부딪히는 경우 추가해야함.
    if ni < 1 or ni > n or nj <1 or nj > n or (ni,nj) in snakes :
        print(time)
        break 

    snakes.appendleft((ni,nj))
    
    if (ni,nj) not in apples:
        snakes.pop()
    else:
        apples.remove((ni,nj))

    if len(change_dir) != 0 and time == int(change_dir[0][0]):
        cur_d += 1 if change_dir[0][1] == "D" else -1
        cur_d %= 4
        change_dir.popleft()
else:
    print(10000)


