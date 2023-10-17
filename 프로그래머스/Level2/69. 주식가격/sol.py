from collections import deque

def solution(prices):
    n = len(prices)
    answer = [0]*n
    d = deque()
    for cur_time in range(n):
        cur_price = prices[cur_time]
        while(len(d)>0):
            past_price, past_time = d[-1]
            if past_price > cur_price:
                answer[past_time] = cur_time-past_time
                d.pop()
            else:
                break 
        d.append((cur_price,cur_time))
    while(len(d)>0):
        past_price,past_time = d.pop()
        answer[past_time] = n-1 - past_time
    return answer

print(solution([1, 2, 3, 2, 3]))