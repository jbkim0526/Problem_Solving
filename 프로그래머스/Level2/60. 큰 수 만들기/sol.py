from collections import deque

def solution(number, k):
    answer = ''
    n = len(number)
    i = count = 0
    d = deque()
    while count < k:
        if len(d) + n - i <= k-count:
            return answer
        num = number[i]
        if num == "9":
            answer += "9"
            count += len(d)
            d = deque()
            i += 1
            continue
        d.append(num)
        if len(d) >= k-count+1:
            m = max(d); a = d.index(m) ; answer += m
            count += a 
            for _ in range(a+1): d.popleft()
        i += 1
    
    if count == k and i < n:
        answer += number[i:]

    return answer

print(solution("4177252841",	4))
#print(solution("8"*1000000,	500000))