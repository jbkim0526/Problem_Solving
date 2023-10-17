def solution(e, starts):
    answer = []
    counts = [1]*(e+1)
    dp = [0]*(e+1)
    for i in range(2,e+1):
        for j in range(i,e+1,i):
            counts[j] += 1

    mins = min(starts)
    max_count, max_num = 0,0

    for num in range(e, mins-1, -1):
        count = counts[num]
        if max_count <= count:
            max_num = num
            max_count = count
        dp[num] = max_num 
    for s in starts:
        answer.append(dp[s])
    return answer

print(solution(8,[1,3,7]))