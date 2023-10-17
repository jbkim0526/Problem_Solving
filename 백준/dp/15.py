import sys
input = sys.stdin.readline

A = input()[:-1]
B = input()[:-1]

dp = [0]*(len(A))
for elem in B:
    cum = 0
    for i in range(len(A)):
        if cum < dp[i]:
            cum = dp[i]
        elif elem == A[i]:
            dp[i] = cum+1

print(max(dp))
         
