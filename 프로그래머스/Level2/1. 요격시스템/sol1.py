def solution(targets):
    answer = 1
    N = len(targets)
    dp = [targets[0]]
    
    for i in range(1,N):
        elem = targets[N-i]
        collapse = False
        for j in range(len(dp)):
            a,b = dp[j]
            c,d = elem

            if a < c < b or a < d < b or c < a < d or c < b < d :
                dp[j] = [max(a,c),min(b,d)]
                collapse = True
        if not collapse:
            dp.append(elem)
            answer = answer +1 

    return answer

