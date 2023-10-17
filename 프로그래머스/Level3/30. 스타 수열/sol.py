from collections import Counter, deque

def solution(a):
    answer = -1
    occurences = Counter(a)
    most_occured = sorted(occurences, key=lambda x: (-occurences[x], x))

    def getStarLength(target):
        ans = 0
        s = deque()
        for num in a:
            s.append(num)
            if len(s) == 1:
                continue 
            if s[0] == s[1] or target not in s:
                s.popleft()
                continue
            ans += 1
            s = deque()
        return ans 

    for num in most_occured:
        if occurences[num] < answer:
            break
        start_len = getStarLength(num)
        answer = max(start_len,answer)
    return 2*answer

print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))

