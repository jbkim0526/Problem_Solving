import sys 
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
stars = [tuple(map(int,input().split())) for _ in range(n)]
stars.sort(key = lambda x : x[0])
cur_x = stars[0][0]
new_x = 0

for i in range(n):
    x, y = stars[i]
    if x != cur_x:
        new_x += 1
        cur_x = x 
    stars[i] = (new_x,y)
stars.sort(key= lambda x : -x[1])

dp = [0]*2*n

def query(l,r):
    l += n ; r += n
    res = 0
    while l < r:
        if l & 1:
            res += dp[l]
            l += 1
        if r & 1:
            r -= 1
            res += dp[r]
        
        l >>= 1 ; r >>= 1
    return res 

def update(x,val):
    x += n 
    while x >= 1:
        dp[x] += val
        x >>= 1

ans = 0
max_y = stars[0][1]
cur_y = max_y
x_lists = defaultdict(int)

for x,y in stars:
    # 가장 위층 : 점수계산 불가능
    if y == max_y:
        update(x,1)
        continue

    # 아래층으로 내려간 경우
    if cur_y != y: 
        # 위층의 x들을 seg tree에 추가
        for nx,count in x_lists.items():
            update(nx,count)
        cur_y = y
        x_lists = defaultdict(int)
   
    c1 = query(0,x)
    c2 = query(x+1,n)
    ans += c1*c2
    x_lists[x] += 1
   
ans %= int(1e9)+7
print(ans)
   
        





     
