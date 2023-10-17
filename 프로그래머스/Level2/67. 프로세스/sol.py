from collections import deque

def solution(priorities, location):
    answer = 1
    d = deque(priorities)
    while True:
        m = max(d)
        n = len(d)
        while d[0] != m:
            d.rotate(-1)
            location = (location-1)%n
        if location == 0:
            break
        d.popleft()
        location -= 1
        answer += 1
    return answer

print(solution([2, 1, 3, 2]	,1))