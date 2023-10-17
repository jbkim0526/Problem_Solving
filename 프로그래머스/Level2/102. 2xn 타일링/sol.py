


def solution(n):
    dp1,dp2 = 1,2
    if n == 1: return dp1 
    elif n == 2: return dp2

    for i in range(3,n+1):
        temp = dp1+dp2 
        dp1 = dp2 
        dp2 = temp
    return dp2 % 1000000007

print(solution(69000))