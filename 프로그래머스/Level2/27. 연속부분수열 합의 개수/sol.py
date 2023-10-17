def solution(elements):
    answer = 0

    n = len(elements)
    d = {}

    for i in range(n):
        s = 0
        for j in range(n):
            s += elements[(i+j) % n ]
            if s not in d:
                d[s] = 0

    answer = len(d)
    return answer


print(solution([7,9,1,1,4]))