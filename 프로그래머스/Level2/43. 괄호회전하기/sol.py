from collections import deque
pairs = {"{":"}", "(":")","[":"]"}

def isValid(x):
    d = deque()
    for char in x:
        if len(d) == 0 :
            d.append(char)
        else: 
            t = d.pop()
            if t not in pairs or pairs[t] != char:
                d.append(t)
                d.append(char)
    return len(d) == 0

def solution(s):
    answer = 0
    l = len(s)
    sd = deque(s)
    for _ in range(l):
        if isValid(sd):
            answer += 1
        sd.append(sd.popleft())
    return answer


print(solution("[](){}"))
