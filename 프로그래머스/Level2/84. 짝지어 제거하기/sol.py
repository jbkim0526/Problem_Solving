from collections import deque

def solution(s):

    left = deque()
    right = deque(s)
    while len(right) > 0:
        a = right.popleft()
        if len(right) == 0:
            left.append(a)
        else:
            b = right.popleft()
            if a == b:
                if len(left) > 0 :
                    right.appendleft(left.pop())
            else:
                left.append(a)
                right.appendleft(b)
    if len(left) > 0:
        return 0
    else:
        return 1

print(solution("cdcd"))
    

        