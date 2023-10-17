from collections import deque

def solution(queue1, queue2):
    answer = -1
    n = len(queue1)
    s1,s2 = sum(queue1),sum(queue2)
    total = s1 + s2
    d1,d2= deque(queue1),deque(queue2)
    
    if total % 2 == 0 :
        target = total // 2
        answer = 0
        while s1 != s2:
            if answer > 3*n:
                return -1
            if s1 > s2:
                t = d1.popleft()
                d2.append(t)
                s1 -= t
                s2 += t
            else:
                t = d2.popleft()
                d1.append(t)
                s1 += t
                s2 -= t
            answer += 1
    return answer

print(solution([1, 1]	,[1, 5]))