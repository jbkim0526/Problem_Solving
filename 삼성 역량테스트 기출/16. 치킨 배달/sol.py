# 미리 집이랑 치킨집의 거리를 다 계산해놓고 사용하면 더 빠르게 할 수 있음
# 알긴 알았는데 구현의 귀찮은 때매 안함 -> 꼭 다시 하기.

import sys 
from math import inf
input = sys.stdin.readline

n,m = map(int,input().split())

b = [list(map(int,input().split())) for _ in range(n)]

chickens = []
houses = []
for i in range(n):
    for j in range(n):
        if b[i][j] == 2:
            chickens.append((i,j))
        if b[i][j] == 1:
            houses.append((i,j))
count = len(chickens)

# 
ans = inf

def track(start, l):
    global ans
    if len(l) == m:
        cur_ans = 0
        for hi,hj in houses:
            chicken_dis = inf
            for ci,cj in l:
                chicken_dis = min(chicken_dis,abs(ci-hi)+abs(cj-hj))
            cur_ans += chicken_dis
        ans = min(cur_ans,ans)
    for i in range(start,count):
        l.append(chickens[i])
        track(i+1,l)
        l.pop()

track(0,[])

print(ans)







