from math import ceil
from collections import Counter
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    l = [ceil((100-progresses[0])/speeds[0])]
    for i in range(1,n):
        l.append(max(l[i-1],ceil((100-progresses[i])/speeds[i])))

    counts = Counter(l)
    for key, value in counts.items():
        answer.append(value)
    return answer

print(solution([93, 30, 55],	[1, 30, 5]))