def solution(n):
    dp = [0,1,1]
    for i in range(2,n):
        dp.append(dp[-1]+dp[-2])
    return dp[n] % 1234567

print(solution(4))