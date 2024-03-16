def solution(n, tops):
    answer = 0

    N = 2*n+1
    blocks = [0 for _ in range(N)]
    
    for i,top in enumerate(tops):
        blocks[2*i+1] = top
    
    dp = [[0 for _ in range(3)] for _ in range(N)]

    dp[0][:] = [1,0,0]
    dp[1][:] = [1,1,1] if blocks[1] else [1,1,0]

    for i in range(2,N):
        if blocks[i]:
             dp[i][0] = sum(dp[i-1][:]) % 10007
             dp[i][1] = sum(dp[i-2][:]) % 10007
             dp[i][2] = sum(dp[i-1][:]) % 10007
        else:
            dp[i][0] = sum(dp[i-1][:]) % 10007
            dp[i][1] = sum(dp[i-2][:]) % 10007
            dp[i][2] = 0

    return sum(dp[N-1][:]) % 10007


print(solution(4, [1, 1, 0, 1]))
print(solution(2, [0, 1]))