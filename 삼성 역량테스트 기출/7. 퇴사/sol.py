import sys 
input = sys.stdin.readline


n = int(input())
infos = []

for _ in range(n):
    infos.append(tuple(map(int,input().split())))

dp = [0]*(n+1)


for i in range(n):
    time, money = infos[i]
    if i+time <= n:
        for j in range(i+time,n+1):
         dp[j] = max(dp[j],dp[i]+money)

print(dp[-1])
