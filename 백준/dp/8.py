import sys 
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))    

dp = [l[0][0]]

for i in range(1,n):
    floor = l[i]
    len_floor = len(floor)
    temp = [0]*len_floor
    for j in range(len_floor):
        v = floor[j]
        if j == 0:
            temp[j] =  dp[j] + v
        elif j == len_floor-1:
            temp[j] =  dp[j-1] + v
        else:
            temp[j] = max(dp[j-1]+v,dp[j]+v)
    dp = temp

print(max(dp))
