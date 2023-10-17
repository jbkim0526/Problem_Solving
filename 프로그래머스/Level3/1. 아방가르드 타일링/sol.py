def solution(n):
    dp = [1,1,3,10]
    if n in [1,2,3]:
        return dp[n]
    l = [0,1,2,5]
    d_sum = [4,2,2]

    for i in range(4,n+1):
        s = 0
        for j in range(1,4):
            s += dp[i-j]*l[j]
        s += d_sum[i % 3]
        dp.append(s % 1000000007)
        for j in range(3):
            if j == 0:
                d_sum[(i+j)%3] += 4*dp[-4]
            else:
                d_sum[(i+j)%3] += 2*dp[-4]
    return dp[-1] 

print(solution(10))