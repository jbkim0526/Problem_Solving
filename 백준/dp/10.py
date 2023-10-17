import sys
input = sys.stdin.readline

n = int(input())

dp = [0,1,1,1,1,1,1,1,1,1]

for i in range(1,n):
    temp = [0]*10
    for j in range(0,10):
        if j == 0:
            temp[j] = dp[j+1]
        elif j == 9:
            temp[j] = dp[j-1]
        else:
            temp[j] = dp[j+1]+dp[j-1]
    dp = temp 
print(sum(dp)%1000000000)