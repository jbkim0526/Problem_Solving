
def solution(n):
    answer = 0
    if n % 2 == 0:

        dp = [0,3,11]
        n //=2 
        if n in [1,2]:
            answer = dp[n]
        else:
            for i in range(3,n+1):
                s = 0
                for j in range(1,i):
                    if i-j == 1: s += dp[j]*3
                    else: s += dp[j]*2
                s += 2
                dp.append(s) 
            answer = dp[-1] 
    return answer % 1000000007


print(solution(6))

