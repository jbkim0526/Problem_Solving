def solution(x, y, n):
    answer = 0

    dp =  [-1]*(y+1)
    dp[x] = 0
    for i in range(x,y):

        if dp[i] == -1:
            continue 
        d = dp[i] + 1

        if i + n <= y:
            if dp[i+n] == -1:
                dp[i+n] = d
            else:
                dp[i+n] = min(dp[i+n],d)
        if 2*i <= y:
         
            if dp[2*i] == -1:
                dp[2*i] = d
            else:
                dp[2*i] = min(dp[2*i],d) 
        if 3*i <= y:
            if dp[3*i] == -1:
                dp[3*i] = d
            else:
                dp[3*i] = min(dp[3*i],d)
    
    answer = dp[y]
    return answer

print(solution(2, 5, 4))