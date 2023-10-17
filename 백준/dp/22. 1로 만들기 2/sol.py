from collections import defaultdict
from math import inf
import sys 
input = sys.stdin.readline 

N = int(input())
dp = [0,0]+[inf]*(N-1)
paths = defaultdict(list)
paths[1].append("1")

for i in range(N+1):
    nums = [i+1,2*i,3*i]
    for num in nums:
        if num > N:
            continue 
        if dp[num] > dp[i]+1:
            dp[num] = dp[i]+1
            paths[num] = [str(num)] + paths[i]
    if 0 < i < N:
        del paths[i]
        
print(dp[N])
print(" ".join(paths[N]))

