def solution(n):
    dp = [1,2]
    i = 2
    while i < n:
        dp.append(dp[i-1]+dp[i-2])
        i += 1
    return dp[n-1] % 1234567