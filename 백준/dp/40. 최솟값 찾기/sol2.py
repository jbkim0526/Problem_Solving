import sys
from collections import deque
input = sys.stdin.readline 

n, l = map(int, input().split())
numbers = list(map(int, input().split()))
d = deque()

res = []
for i, num in enumerate(numbers):
    while d and d[-1][1] > num: d.pop()
    while d and d[0][0] <= i-l: d.popleft()
    d.append((i,num))
    res.append(d[0][1])

print(*res)
    



