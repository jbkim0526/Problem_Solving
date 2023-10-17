def solution(citations):
    answer = 0
    citations.sort(key = lambda x: -x)
    for i in range(len(citations)):
        if i+1 <= citations[i]:
            answer = i+1

    return answer


print(solution([3, 0, 6, 1, 5]))