from math import inf
from collections import defaultdict
def solution(N, number):
    answer = 0

    dp = defaultdict(lambda: inf)
    num = 0
    num_list = [1]
    cost_list= [2]

    for i in range(5):
        num = 10*num+N 
        if num > number:
            break 
        num_list.append(num)
        cost_list.append(i+1)
        dp[num] = i+1

    if N == 1: 
        dp[1] = 1
        cost_list[0] = 1
    else:
        dp[1] = 2

    print(num_list)
    print(cost_list)
    print(dp)
    # 상한을 어떻게????
    # addition and multiplication first
    for num in range(2,number+1):
        candidates = [dp[num]]
        # num를 덧셈으로 만드려면 1+i-1 + ....
        for i in range(1,num//2+1):
            if dp[i] == -1 or dp[num-i] == -1:
                continue
            candidates.append(dp[i] + dp[num-i])
        # num을 곱셈으로 만드려면 
        for i in range(2, int(num**(1/2)+1)):
            if num % i != 0:
                continue
            if dp[i] == -1 or dp[num//i] == -1:
                continue
            candidates.append(dp[i]*dp[num//i])
        if len(candidates) == 0:
            continue
        min_val = min(candidates)
        print(num,candidates)
        dp[num] = min_val if min_val <= 8 else -1

    print(dp)

    return answer
print(solution(5, 12))
#print(solution(1, 31168))