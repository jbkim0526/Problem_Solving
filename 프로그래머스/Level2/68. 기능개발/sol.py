from math import ceil
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    l = [ceil((100-progresses[0])/speeds[0])]
    for i in range(1,n):
        l.append(max(l[i-1],ceil((100-progresses[i])/speeds[i])))

    temp = l[0] ; count = 1
    for i in range(1,n):
        if temp == l[i]:
            count += 1
        else:
            answer.append(count)
            temp = l[i]
            count = 1
    answer.append(count)

    return answer

print(solution([93, 30, 55],	[1, 30, 5]))