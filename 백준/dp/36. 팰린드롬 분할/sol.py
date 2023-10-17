import sys 
from collections import deque
input = sys.stdin.readline 

sequence = input()[:-1]
n = len(sequence)
dp = [2500 for _ in range(n + 1)]
dp[-1] = 0

pelin_list =  [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    l,r = i,i
    while 0 <= l and r <= n-1:
        if sequence[l] != sequence[r]:
            break 
        pelin_list[l][r] = True
        l -= 1
        r += 1

    l,r = i, i+1 
    while 0 <= l and r <= n-1:
        if sequence[l] != sequence[r]:
            break 
        pelin_list[l][r] = True
        l -= 1
        r += 1

for end in range(n):
    for start in range(end+1):
        if pelin_list[start][end]:
            dp[end] = min(dp[end], dp[start - 1] + 1)
        else:
            dp[end] = min(dp[end], dp[end - 1] + 1)

print(dp[n-1])





